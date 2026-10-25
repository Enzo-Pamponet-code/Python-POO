class Print_:
    """
     Imprima objeto(s) fornecido(s) via argumentos posicionais.
     Essa função tem uma assinatura idêntica à impressão embutida.
     Para recursos mais avançados, veja a classe :class:'~rich.console.Console'.
     Args:
      sep (força, opcional): Separador entre objetos impressos. Padrão para "".
      end (força, opcional): Caractere a escrever no final da saída. Padrão para "\\n".
      file (IO, opcional): file para escrever, ou None para stdout. Padrão para nenhum.
      Flush (bool, opcional): Não tem efeito porque Rich sempre descarrega a saída.
    O padrão é \033[31mFalse\033[m.
    Marcação do Console

    Rich suporta uma marcação simples que você pode usar para inserir cores e estilos virtualmente em todos os lugares Rich aceitaria uma string (por exemplo, print()e log()).

    Execute o seguinte comando para ver alguns exemplos:

    python -m rich.markup

    Sintaxe

    A marcação de console usa uma sintaxe inspirada no código bb. Se você escrever o estilo (veja Estilos) entre colchetes, por exemplo. [bold red], esse estilo será aplicado até que seja fechado com um correspondente [/bold red].

    Aqui está um exemplo simples:

    from rich import print
    print("[bold red]alert![/bold red] Something happened")

    Se você não fechar um estilo, ele será aplicado até o final da string. O que às vezes é conveniente se você quiser estilizar uma única linha. Por exemplo:

    print("[bold italic yellow on red blink]This text is impossible to read")

    Há uma abreviação para fechar um estilo. Se você omitir o nome do estilo da tag de fechamento, Rich fechará o último estilo. Por exemplo:

    print("[bold red]Bold and red[/] not bold or red")

    Essas tags de marcação podem ser usadas em combinação entre si e não precisam ser estritamente aninhadas. O exemplo a seguir demonstra a sobreposição de tags de marcação:

    print("[bold]Bold[italic] bold and italic [/bold]italic[/italic]")

    erros

    Rich vai levantar MarkupErrorse a marcação contiver um dos seguintes erros:

        Tags incompatíveis, por exemplo. "[bold]Hello[/red]"

        Nenhuma etiqueta correspondente para o fechamento implícito, por exemplo. "no tags[/]"

    Links

    A marcação do console pode gerar hiperlinks com a seguinte sintaxe: [link=URL]text[/link]. Veja um exemplo:

    print("Visit my [link=https://www.willmcgugan.com]blog[/link]!")

    Se o seu software de terminal suportar hiperlinks, você poderá clicar na palavra “blog” que normalmente abrirá um navegador. Se o seu terminal não suportar hiperlinks, você verá o texto, mas não será clicável.
    Escapar

    Ocasionalmente, você pode querer imprimir algo que Rich interpretaria como marcação. Você pode escapar de uma tag precedendo-a com uma barra invertida. Veja um exemplo:

    from rich import print
    print(r"foo\[bar]")
    foo[bar]

    Sem a reação, Rich assumirá isso [bar]é uma tag e removê-lo da saída se não houver estilo “bar”.

    Nota

    Se você quiser evitar que a barra invertida escape da tag e produza uma barra invertida literal antes de uma tag, você pode inserir duas barras.

    A função escape()lidará com a fuga de texto para você.

    Escapar é importante se você construir a marcação de console dinamicamente, com str.formatou f strings (por exemplo). Sem escapar pode ser possível injetar tags onde você não as deseja. Considere a seguinte função:

    def greet(name):
        console.print(f"Hello {name}!")

    Chamando greet("Will")vai imprimir uma saudação, mas se você fosse chamar greet("[blink]Gotcha![/blink]")então você também obterá texto piscando, o que pode não ser desejável. A solução é fugir dos argumentos:

    from rich.markup import escape
    def greet(name):
        console.print(f"Hello {escape(name)}!")

    Emoji

    Se você adicionar um código de emoji para marcação, ele será substituído pelo caractere unicode equivalente. Um código de emoji consiste no nome do emoji cercado ser cólons (:). Veja um exemplo:

    from rich import print
    print(":warning:")
    ⚠️

    Alguns emojis têm duas variantes, a variante “emoji” é exibida em cores completas e a variante “texto” é exibida em monocromático (como que suas cores padrão estejam definidas). Você pode especificar a variante desejada adicionando qualquer “-emoji” ou “-texto” para o código emoji. Veja um exemplo:

    from rich import print
    print(":red_heart-emoji:")
    print(":red_heart-text:")

    Para ver uma lista de todos os emojis disponíveis, execute o seguinte comando:

    python -m rich.emoji

    Marcação de renderização

    Por padrão, o Rich renderizará a marcação do console quando você passar explicitamente uma string para print()ou implicitamente quando você incorpora uma string em outro objeto rentrável, como Tableou Panel.

    A marcação do console é conveniente, mas você pode desejá-la se a sintaxe entrar em conflito com a string que deseja imprimir. Você pode fazer isso configurando markup=Falsesobre o print()método ou sobre o Consoleconstrutor.
    API de marcação

    Você pode converter uma string em texto estilizado chamando from_markup(), que retorna a Textinstância que você pode imprimir ou adicionar mais estilos para.

    """


g1 = Print_()
print(g1.__doc__)