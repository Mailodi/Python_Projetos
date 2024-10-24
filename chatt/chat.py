import flet as ft

def main_app(page):
    title_main = ft.Text("MChat")
    page.add(title_main)
    
    def send_mensage_tunel(mensagem):
        text = ft.Text(mensagem)
        chat.controls.append(text)
        page.update()
        
    page.pubsub.subscribe(send_mensage_tunel)
    
    def fun_send_message(event):
        name_user = box_name.value
        fild_text_message = send_menssage.value
        get_text = f"{name_user}: {fild_text_message}"
        page.pubsub.send_all(get_text)
        send_menssage.value = ""
        page.update()
    
    send_menssage = ft.TextField(label = "Digite sua mensagem")
    buttom_send = ft.ElevatedButton("Enviar", on_click= fun_send_message)
    line_send = ft.Row([send_menssage, buttom_send])
    
    chat = ft.Column()
    
    title_popup = ft.Text("Bem vindo ao MChat")
    box_name = ft.TextField(label="Digite o seu nome")
    
    def enter_chat(event):
        popup.open = False
        page.remove(title_main)
        page.remove(button_start)
        page.add(chat)
        page.add(line_send)
        
        name_user = box_name.value
        text_message = f"{name_user} entrou no chat"
        page.pubsub.send_all(text_message)
        page.update()
        
    button_popup = ft.ElevatedButton("Entrar no Chat", on_click= enter_chat)
    
    popup = ft.AlertDialog(title = title_popup, content=box_name, actions=[button_popup])
    
    def open_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    button_start = ft.ElevatedButton("Iniciar Chat", on_click=open_popup)
    page.add(button_start)

ft.app(main_app, view=ft.AppView.WEB_BROWSER)