# ==========================
# VARIÁVEIS DO CHAT
# ==========================

default bit_chat_open = False
default bit_input = ""
default bit_response = ""


# ==========================
# BOTÃO DO BIT NO CANTO DA TELA
# ==========================

screen bit_button():

    zorder 100

    frame:
        background None
        xalign 1.0
        yalign 1.0
        xoffset -30
        yoffset -30

        imagebutton:
            idle "gui/bit_icon.png"
            hover "gui/bit_icon.png"
            action ToggleVariable("bit_chat_open")
            insensitive "gui/bit_icon.png"


# ==========================
# TELA DO CHAT DO BIT
# ==========================

screen bit_chat():

    if bit_chat_open:

        frame:
            background "#1d1d1ddd"
            xalign 1.0
            yalign 0.5
            xsize 450
            ysize 600
            xoffset -50
            padding (20, 20, 20, 20)

            vbox:
                spacing 10

                text "Bit — Assistente de Python" size 28 color "#00ff55"
                text "Digite algo para o Bit..." size 20 color "#ffffff"

                # ✅ CORRIGIDO
                input value VariableInputValue("bit_input") color "#ffffff" size 20

                textbutton "Enviar":
                    action Function(_enviar_para_bit)

                if bit_response:
                    text bit_response size 20 color "#00ffdd"

# ==========================
# OVERLAYS DO JOGO
# ==========================

init python:
    config.overlay_screens.append("bit_button")
    config.overlay_screens.append("bit_chat")

    def _enviar_para_bit():
        import bit_ai
        pergunta = store.bit_input.strip()
        if not pergunta:
            store.bit_response = "Por favor, escreva uma pergunta."
        else:
            store.bit_response = "Pensando..."
            store.bit_response = bit_ai.perguntar_ao_bit(pergunta)
            store.bit_input = ""