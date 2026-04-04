// Cloudflare Pages Function - Contact Form Handler
export async function onRequestPost(context) {
  const formData = await context.request.formData();
  
  const name = formData.get('name');
  const email = formData.get('email');
  const category = formData.get('category');
  const message = formData.get('message');

  // Validate
  if (!name || !email || !category || !message) {
    return new Response(JSON.stringify({ success: false, error: 'Alle Felder erforderlich' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
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

  const categoryLabel = categoryLabels[category] || category;

  // Send email using MailChannels (free on Cloudflare)
  try {
    const emailResponse = await fetch('https://api.mailchannels.net/tx/v1/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        personalizations: [{
          to: [{ email: 'info@masspost.store', name: 'MediaMass Support' }],
          reply_to: { email: email, name: name }
        }],
        from: {
          email: 'noreply@masspost.store',
          name: 'MediaMass Kontaktformular'
        },
        subject: `[MediaMass Kontakt] ${categoryLabel} - ${name}`,
        content: [{
          type: 'text/plain',
          value: `
Neue Kontaktanfrage von MediaMass Website
==========================================

Von: ${name}
E-Mail: ${email}
Kategorie: ${categoryLabel}

Nachricht:
----------
${message}

==========================================
Gesendet über: www.masspost.store/contact.html
Zeitstempel: ${new Date().toLocaleString('de-DE', { timeZone: 'Europe/Berlin' })}
          `.trim()
        }]
      })
    });

    if (emailResponse.ok) {
      return new Response(JSON.stringify({ success: true, message: 'Erfolgreich gesendet!' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    } else {
      throw new Error('MailChannels API error');
    }
  } catch (error) {
    return new Response(JSON.stringify({ success: false, error: 'Fehler beim Senden' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
