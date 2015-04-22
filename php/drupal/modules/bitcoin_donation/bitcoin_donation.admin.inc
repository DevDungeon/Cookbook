<?php
/**
 * Bitcoin Donation
 * 
 * Add a Bitcoin Donation widget to your website
 * 
 * Written by nanodano@devdungeon.com
 *
 */


/**
 * Menu callback; Displays the administration settings for Bitcoin Donation.
 */
function bitcoin_donation_admin_settings() {
  $form = array();
  $form['bitcoin_donation_receive_address'] = array(
    '#type' => 'textfield',
    '#title' => t('Bitcoin Receive Address'),
    '#description' => t('The receive Bitcoin address to get donations'),
    '#default_value' => variable_get('bitcoin_donation_receive_address', 0),
  );
  return system_settings_form($form);
}

