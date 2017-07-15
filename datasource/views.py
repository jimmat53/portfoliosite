from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ascii_art = """
    <link rel="shortcut icon" type="image/png" href="{{STATIC_URL}}/favicon.ico"/>
    <pre>

  ________  _____    __    __       __    __      ____  ________  __    __  _____ ___       ___     _____    ____    ______  ________  _________  ____   _____     _____   ____ _______
 (___  ___)(_   _)   \ \  / /       \ \  / /     (    )(___  ___)(  \  /  )/ ___/(  (       )  )   (  __ \  / __ \  (   __ \(___  ___)(_   _____)/ __ \ (_   _)   (_   _) / __ \\     /
     ) )     | |     () \/ ()       () \/ ()     / /\ \    ) )    \ (__) /( (__   \  \  _  /  /     ) )_) )/ /  \ \  ) (__) )   ) )     ) (___  / /  \ \  | |       | |  / /  \ \\   /
    ( (      | |     / _  _ \       / _  _ \    ( (__) )  ( (      ) __ (  ) __)   \  \/ \/  /     (  ___/( ()  () )(    __/   ( (     (   ___)( ()  () ) | |       | | ( ()  () )) (
 __  ) )     | |    / / \/ \ \     / / \/ \ \    )    (    ) )    ( (  ) )( (       )   _   (       ) )   ( ()  () ) ) \ \  _   ) )     ) (    ( ()  () ) | |   __  | | ( ()  () )\_/
( (_/ /     _| |__ /_/      \_\   /_/      \_\  /  /\  \  ( (      ) )( (  \ \___   \  ( )  /      ( (     \ \__/ / ( ( \ \_)) ( (     (   )    \ \__/ /__| |___) )_| |__\ \__/ /  _
 \___/     /_____((/          \) (/          \)/__(  )__\ /__\    /_/  \_\  \____\   \_/ \_/       /__\     \____/   )_) \__/  /__\     \_/      \____/ \________//_____( \____/  (_)


 __                   __.
/  ` _ ._ _ *._  _   (__  _  _ ._
\__.(_)[ | )|[ )(_]  .__)(_)(_)[ )******
                ._|


    </pre>"""
    return HttpResponse("<b>" + ascii_art + "</b>")


