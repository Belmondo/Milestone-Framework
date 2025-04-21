<?php

// Função para decodificar a mensagem usando AES
function decodeAES($message, $key) {
    $cipher = "aes-256-cbc";
    $ivlen = openssl_cipher_iv_length($cipher);
    $iv = openssl_random_pseudo_bytes($ivlen);
    $decrypted = openssl_decrypt(base64_decode($message), $cipher, $key, OPENSSL_RAW_DATA, $iv);
    return $decrypted;
}

// Função para decodificar a mensagem usando DES
function decodeDES($message, $key) {
    $cipher = "des-ede3-cbc";
    $ivlen = openssl_cipher_iv_length($cipher);
    $iv = openssl_random_pseudo_bytes($ivlen);
    $decrypted = openssl_decrypt(base64_decode($message), $cipher, $key, OPENSSL_RAW_DATA, $iv);
    return $decrypted;
}

// Função para simular o controle de uma lâmpada
function controlLamp($action, $intensity) {
    if ($action == "on") {
        return "Lâmpada ligada com intensidade de luz $intensity%";
    } elseif ($action == "off") {
        return "Lâmpada desligada";
    } else {
        return "Ação inválida";
    }
}

// Função para simular o controle de uma tomada
function controlSocket($action) {
    if ($action == "on") {
        return "Tomada ligada";
    } elseif ($action == "off") {
        return "Tomada desligada";
    } else {
        return "Ação inválida";
    }
}

// Função para simular a conexão com uma caixa de som
function controlSpeaker($action) {
    if ($action == "connect") {
        return "Caixa de som conectada";
    } elseif ($action == "disconnect") {
        return "Caixa de som desconectada";
    } else {
        return "Ação inválida";
    }
}

// Função para simular o controle de um ar-condicionado
function controlAC($action, $temperature) {
    if ($action == "on") {
        return "Ar-condicionado ligado com temperatura de $temperature °C";
    } elseif ($action == "off") {
        return "Ar-condicionado desligado";
    } else {
        return "Ação inválida";
    }
}

// Inicializa o array para resposta JSON
$response = array();

// Recebendo os parâmetros via POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Verificando o tipo de controle solicitado
    if (isset($_POST["control"])) {
        $control = $_POST["control"];

        // Executando a função correspondente ao tipo de controle
        switch ($control) {
            case "lamp":
                $action = $_POST["action"];
                $intensity = $_POST["intensity"];
                $response['lamp_status'] = controlLamp($action, $intensity);
                break;
            case "socket":
                $action = $_POST["action"];
                $response['socket_status'] = controlSocket($action);
                break;
            case "speaker":
                $action = $_POST["action"];
                $response['speaker_status'] = controlSpeaker($action);
                break;
            case "ac":
                $action = $_POST["action"];
                $temperature = $_POST["temperature"];
                $response['ac_status'] = controlAC($action, $temperature);
                break;
            default:
                $response['error'] = "Tipo de controle inválido";
        }
    } else {
        $response['error'] = "Tipo de controle não especificado";
    }
}

// Retornando a resposta como JSON
header('Content-Type: application/json');
echo json_encode($response);
?>
