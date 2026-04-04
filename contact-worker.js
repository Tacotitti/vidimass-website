// Cloudflare Worker for Contact Form Email Forwarding
// Deploy this to Cloudflare Workers and connect to your Pages site

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // CORS headers for frontend
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  }

  // Handle CORS preflight
  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders })
  }

  // Only accept POST requests
  if (request.method !== 'POST') {
    return new Response('Method not allowed', { 
      status: 405,
      headers: corsHeaders 
    })
  }

  try {
    // Parse form data
    const formData = await request.json()
    const { name, email, category, message } = formData

    // Validate required fields
    if (!name || !email || !category || !message) {
      return new Response(JSON.stringify({ 
        success: false, 
        error: 'Alle Felder sind erforderlich' 
      }), {
        status: 400,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      })
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(email)) {
      return new Response(JSON.stringify({ 
        success: false, 
        error: 'Ungültige E-Mail-Adresse' 
      }), {
        status: 400,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      })
    }

    // Category labels
    const categoryLabels = {
      'tiktok': 'TikTok Mass Posting',
      'spotify': 'Spotify Charting',
      'instagram': 'Instagram Mass Posting',
      'multi': 'Multi-Plattform',
      'label': 'Musik-Label/Artist Charting',
      'enterprise': 'Unternehmen',
      'other': 'Sonstiges'
    }

    // Prepare email content
    const emailSubject = `[MediaMass Kontakt] ${categoryLabels[category] || category} - ${name}`
    const emailBody = `
Neue Kontaktanfrage von MediaMass Website
==========================================

Von: ${name}
E-Mail: ${email}
Kategorie: ${categoryLabels[category] || category}

Nachricht:
----------
${message}

==========================================
Gesendet über: www.masspost.store/contact.html
Zeitstempel: ${new Date().toLocaleString('de-DE', { timeZone: 'Europe/Berlin' })}
    `.trim()

    // Send email using Cloudflare Email Routing API
    // Note: You need to configure this in Cloudflare dashboard first
    const emailResponse = await fetch('https://api.mailchannels.net/tx/v1/send', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        personalizations: [
          {
            to: [{ email: 'info@masspost.store', name: 'MediaMass Support' }],
            reply_to: { email: email, name: name }
          }
        ],
        from: {
          email: 'noreply@masspost.store',
          name: 'MediaMass Kontaktformular'
        },
        subject: emailSubject,
        content: [
          {
            type: 'text/plain',
            value: emailBody
          }
        ]
      })
    })

    if (!emailResponse.ok) {
      throw new Error('Email sending failed')
    }

    // Success response
    return new Response(JSON.stringify({ 
      success: true, 
      message: 'Nachricht erfolgreich gesendet!' 
    }), {
      status: 200,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    })

  } catch (error) {
    console.error('Contact form error:', error)
    return new Response(JSON.stringify({ 
      success: false, 
      error: 'Fehler beim Senden der Nachricht. Bitte versuchen Sie es später erneut oder kontaktieren Sie uns direkt per E-Mail.' 
    }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    })
  }
}
