    <!-- Favicons -->
    <link href="{{ url_for('static', filename='/favicon.ico') }}" rel="icon">

    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Overpass">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='assets/css/style.css') }}">
    <title>One Tap</title>
</head>
<body>

    {% block navbar %}

    <div class="container-fluid" style="background-color: #000;">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top shadow-sm">

            <!--  Show this only on mobile to medium screens  -->
              <a class="navbar-brand d-lg-none" href="{{ url_for('home') }}"><b class="lg"><span class="logo">One</span> Tap</b></a>
            
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
            
            <!--  Use flexbox utility classes to change how the child elements are justified  -->
              <div class="collapse navbar-collapse justify-content-between" id="navbarToggle">
            
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('headlines') }}">Headlines</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link"href="{{ url_for('articles') }}">Articles</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link"href="{{ url_for('sources') }}">Sources</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-expanded="false">
                          Categories
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                          <a class="dropdown-item" href="{{ url_for('business') }}">Business</a>
                          <a class="dropdown-item" href="{{ url_for('tech') }}">Technology</a>
                          <a class="dropdown-item" href="{{ url_for('entertainment') }}">Entertainment</a>
                          <a class="dropdown-item" href="{{ url_for('science') }}">Science</a>
                          <a class="dropdown-item" href="{{ url_for('sports') }}">Sport</a>
                          <a class="dropdown-item" href="{{ url_for('health') }}">Health</a>
                        </div>
                    </li>
                </ul>
                
                
            <!--   Show this only lg screens and up   -->
                <a class="navbar-brand d-none d-lg-block" href="{{ url_for('home') }}"><b class="lg"><span class="logo">One</span> Tap</b></a>
                
                
                
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="/headlines">
                            <svg class="svg" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;"><path d="M16.5,8c0,1.5-0.5,3.5-2.9,4.3c0.7-1.7,0.8-3.4,0.3-5c-0.7-2.1-3-3.7-4.6-4.6C8.9,2.4,8.2,2.8,8.3,3.4c0,1.1-0.3,2.7-2,4.4  C4.1,10,3,12.3,3,14.5C3,17.4,5,21,9,21c-4-4-1-7.5-1-7.5c0.8,5.9,5,7.5,7,7.5c1.7,0,5-1.2,5-6.4c0-3.1-1.3-5.5-2.4-6.9  C17.3,7.2,16.6,7.5,16.5,8"></path></svg>
                        </a>
                    </li>
                                        <li class="nav-item">
                        <a class="nav-link" href="/Login">
                            <svg class="svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;"><path d="M12 2A10.13 10.13 0 0 0 2 12a10 10 0 0 0 4 7.92V20h.1a9.7 9.7 0 0 0 11.8 0h.1v-.08A10 10 0 0 0 22 12 10.13 10.13 0 0 0 12 2zM8.07 18.93A3 3 0 0 1 11 16.57h2a3 3 0 0 1 2.93 2.36 7.75 7.75 0 0 1-7.86 0zm9.54-1.29A5 5 0 0 0 13 14.57h-2a5 5 0 0 0-4.61 3.07A8 8 0 0 1 4 12a8.1 8.1 0 0 1 8-8 8.1 8.1 0 0 1 8 8 8 8 0 0 1-2.39 5.64z"></path><path d="M12 6a3.91 3.91 0 0 0-4 4 3.91 3.91 0 0 0 4 4 3.91 3.91 0 0 0 4-4 3.91 3.91 0 0 0-4-4zm0 6a1.91 1.91 0 0 1-2-2 1.91 1.91 0 0 1 2-2 1.91 1.91 0 0 1 2 2 1.91 1.91 0 0 1-2 2z"></path></svg> Log In / Register
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>

    {% endblock %}

    {% block content %}

    {% endblock %}

    {% block footer %}

    <div class="container-fluid footer">
        <p class="text-center footer-text">
            © <span class="logo">News</span> NEWS TRACKER APPLICATION
        </p>
    </div>

    {% endblock %}

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/js/bootstrap.min.js"></script>
    <script>
        window.watsonAssistantChatOptions = {
          integrationID: "fa18fb77-6c75-43f6-b1a1-a4f29fbbbc16", // The ID of this integration.
          region: "eu-gb", // The region your integration is hosted in.
          serviceInstanceID: "87be378b-e186-46e4-9050-a97b5f524d5b", // The ID of your service instance.
          onLoad: function(instance) { instance.render(); }
        };
        setTimeout(function(){
          const t=document.createElement('script');
          t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
          document.head.appendChild(t);
        });
      </script>
</body>
</html>
