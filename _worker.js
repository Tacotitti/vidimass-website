// Cloudflare Worker for Contact Form - Uses Resend API
export default {
  async fetch(request) {
    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // Only accept POST
    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ success: false, error: 'Method not allowed' }), {
        status: 405,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }

    try {
      const formData = await request.formData();
      const name = formData.get('name');
      const email = formData.get('email');
      const category = formData.get('category');
      const message = formData.get('message');

      // Validate
      if (!name || !email || !category || !message) {
        return new Response(JSON.stringify({ success: false, error: 'Alle Felder erforderlich' }), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }

      const categoryLabels = {
        'tiktok': 'TikTok Mass Posting',
        'spotify': 'Spotify Charting',
        'instagram': 'Instagram Mass Posting',
        'multi': 'Multi-Plattform',
        'label': 'Musik-Label/Artist Charting',
        'enterprise': 'Unternehmen',
        'other': 'Sonstiges'
      };

      // Send via Resend API (free tier: 100 emails/day)
      const resendResponse = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer re_123456789', // REPLACE WITH YOUR RESEND API KEY
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: 'MediaMass <onboarding@resend.dev>',
          to: 'info@masspost.store',
          reply_to: email,
          subject: `[MediaMass Kontakt] ${categoryLabels[category]} - ${name}`,
          text: `
Neue Kontaktanfrage von MediaMass Website
==========================================

Von: ${name}
E-Mail: ${email}
Kategorie: ${categoryLabels[category]}

Nachricht:
----------
${message}

==========================================
Gesendet über: www.masspost.store/contact.html
Zeitstempel: ${new Date().toLocaleString('de-DE', { timeZone: 'Europe/Berlin' })}
          `.trim()
        })
      });

      if (resendResponse.ok) {
        return new Response(JSON.stringify({ success: true, message: 'Erfolgreich gesendet!' }), {
          status: 200,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      } else {
        throw new Error('Email API error');
      }

    } catch (error) {
      return new Response(JSON.stringify({ success: false, error: 'Server-Fehler' }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
  }
};
