from playwright.sync_api import sync_playwright

import pytest


@pytest.mark.parametrize("browser_type", ["chromium"])
def test_terms_and_conditions(browser_type):

    with sync_playwright() as p:

        # Lancement navigateur
        browser = p.chromium.launch(headless=False)

        # Création contexte utilisateur
        context = browser.new_context()

        # Page principale
        home_page = context.new_page()

        # Ouverture site
        home_page.goto("https://shop.example.com")

        # Vérification page accueil
        assert "Accueil" in home_page.title()

        # Ouverture nouvel onglet
        with home_page.expect_popup() as popup:

            home_page.click("text=Conditions générales")

        # Nouvel onglet
        terms_page = popup.value

        # Attente chargement
        terms_page.wait_for_load_state()

        # Vérification titre
        assert "Conditions" in terms_page.title()

        # Vérification contenu
        text = terms_page.text_content("body")

        assert "Conditions générales" in text

        # Fermer onglet CGV
        terms_page.close()

        # Retour page principale
        home_page.click("#add-cart")

        home_page.click("#checkout")

        # Vérification checkout
        assert "/checkout" in home_page.url

        # Fermeture
        home_page.close()

        browser.close()
