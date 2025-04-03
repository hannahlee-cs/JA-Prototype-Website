# UT Japanese Association Website
#### Description: A website used to compilate different resources for the UT Austin Japanese Association

# HTML-
    Each page in the site is composed of various HTML components including buttons with on-click commands, image galleries with linked-offsite images, and imput boxes.

    ## index.html-
        The main page for the site featuring the links to the other pages of the site. The inter-site navigation relies on buttons with on-click commands that link to the other html pages using flask directing. The main page features two image galleries: the first with a non-interactable main image on the top of the page, and a second with three images with hovering commands designed to simulate interaction.

    ## organization.html-
        The page designed to highlight the organizations associated with the UT Japanese Association. The page features JA, Kaiwa Table, and the language learning podcast associated with the organization. Each featured aspect has an image (with hoverable interaction effects) and a button with an on-click command linking to the associated page where the user can learn more. The page also features a main image showcasing a fundraising event for UT JA.

    ## academic.html-
        The page designed to highlight the academics associated with the UT Japanese Association. The page features a main image and two buttons (with hoverable interaction effects) with on-click commands linking to associated websites.

    ##affiliations.html-
        The page designed to feature JapanLabs, an associated organization giving internship opprotunities for Japanese students (or students intrested in Japanese cultre). The page features a main image with a brief description of the org. There is a hyper-;linked button that links to the org's official website.

    ##thanks.html-
        The page designed to say 'thank you' when the user submits an email to the imput box.

#Flask/python/javaScript
    ##app.py-
        The only file dealing with the flask implementation of the site. The file correctly manages site redirection with on-click commands. 
