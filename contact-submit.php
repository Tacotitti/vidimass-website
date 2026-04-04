<?php
// Contact Form Handler - Direct PHP Email Sending
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');

// Handle OPTIONS request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
    exit();
}

// Get form data
$name = isset($_POST['name']) ? trim($_POST['name']) : '';
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$category = isset($_POST['category']) ? trim($_POST['category']) : '';
$message = isset($_POST['message']) ? trim($_POST['message']) : '';

// Validate required fields
if (empty($name) || empty($email) || empty($category) || empty($message)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Alle Felder sind erforderlich']);
    exit();
}

// Validate email format
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Ungültige E-Mail-Adresse']);
    exit();
}

// Category labels
$categoryLabels = [
    'tiktok' => 'TikTok Mass Posting',
    'spotify' => 'Spotify Charting',
    'instagram' => 'Instagram Mass Posting',
    'multi' => 'Multi-Plattform',
    'label' => 'Musik-Label/Artist Charting',
    'enterprise' => 'Unternehmen',
    'other' => 'Sonstiges'
];

$categoryLabel = isset($categoryLabels[$category]) ? $categoryLabels[$category] : $category;

// Email settings
$to = 'info@masspost.store';
$subject = '[MediaMass Kontakt] ' . $categoryLabel . ' - ' . $name;

// Email body
$emailBody = "Neue Kontaktanfrage von MediaMass Website\n";
$emailBody .= "==========================================\n\n";
$emailBody .= "Von: " . $name . "\n";
$emailBody .= "E-Mail: " . $email . "\n";
$emailBody .= "Kategorie: " . $categoryLabel . "\n\n";
$emailBody .= "Nachricht:\n";
$emailBody .= "----------\n";
$emailBody .= $message . "\n\n";
$emailBody .= "==========================================\n";
$emailBody .= "Gesendet über: www.masspost.store/contact.html\n";
$emailBody .= "Zeitstempel: " . date('d.m.Y H:i:s') . " (Europe/Berlin)\n";
$emailBody .= "IP-Adresse: " . $_SERVER['REMOTE_ADDR'] . "\n";

// Email headers
$headers = "From: MediaMass Kontaktformular <noreply@masspost.store>\r\n";
$headers .= "Reply-To: " . $email . "\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

// Send email
$mailSent = mail($to, $subject, $emailBody, $headers);

if ($mailSent) {
    http_response_code(200);
    echo json_encode([
        'success' => true, 
        'message' => 'Nachricht erfolgreich gesendet!'
    ]);
} else {
    http_response_code(500);
    echo json_encode([
        'success' => false, 
        'error' => 'Fehler beim Senden der E-Mail. Bitte versuchen Sie es später erneut.'
    ]);
}
?>
