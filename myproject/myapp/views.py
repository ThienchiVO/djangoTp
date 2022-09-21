from django.http import HttpResponse
from myapp.models import User


# Create your views here.

def hello(request):
    html = "<p>Hello world, my name is Carl and Thien chi is my boss</p>"
    return HttpResponse(html)


def users(request):
    users_list = User.objects.all()
    html_user_list = """
        <table><thead><tr>
            <th>Id</th>
            <th>Prénom</th>
            <th>Nom</th>
        </tr></thead><tbody>"""
    for user in users_list:
        html_user_list += f"""<tr>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
        </tr>"""
    html_user_list += "</tbody></table>"
    return HttpResponse(html_user_list)
