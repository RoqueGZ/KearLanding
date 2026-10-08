<?php
/** Theme assets; content remains editable in native blocks. */
if ( ! defined( 'ABSPATH' ) ) { exit; }
add_action( 'after_setup_theme', function () {
    add_theme_support( 'editor-styles' );
    add_editor_style( 'style.css' );
} );
add_action( 'init', function () {
    register_block_pattern_category( 'kear-landings', array( 'label' => __( 'KEAR · Landings', 'kear-landings' ) ) );
} );
add_action( 'wp_enqueue_scripts', function () {
    $version = wp_get_theme()->get( 'Version' );
    wp_enqueue_style( 'kear-landings', get_theme_file_uri( 'style.css' ), array(), $version );
    wp_enqueue_script( 'kear-landings', get_theme_file_uri( 'assets/landing.js' ), array(), $version, true );
} );
add_action( 'wp_body_open', function () {
    echo '<a class="skip-link" href="#contenido">Saltar al contenido</a>';
} );
// Provisional local SEO. A later SEO plugin can take ownership of these fields.
add_filter( 'pre_get_document_title', function ( $title ) {
    return is_front_page() ? 'Instalaciones eléctricas para empresas en Santa Fe | KEAR' : $title;
} );
add_action( 'wp_head', function () {
    if ( is_front_page() ) {
        echo '<meta name="description" content="Instalaciones eléctricas, tableros y automatización para empresas en Santa Fe. Contanos tu proyecto y consultá por WhatsApp o formulario.">';
    }
} );
// Spanish commercial copy remains correctly identified without downloaded translations.
add_filter( 'language_attributes', function ( $attributes ) {
    return is_front_page() ? preg_replace( '/lang="[^"]*"/', 'lang="es-AR"', $attributes ) : $attributes;
} );
