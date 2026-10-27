// Código para a página web das Backrooms | Introdução.

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const originalTitle = document.title.split("");

const titlechanges = [
    "!", "N", "+","r̶̸͕͂ͭͅ", "0", "#", "U", "º", "@", "O", " ",
    "|", " ", "§", "A", "[", "K", "&", "0", "0", "m̵̧̠̭̦͉͋́͂͌ͥ͊̾ͨ", "§"
];

const currentTitle = [...originalTitle];

(async function () {
    while (true) {
        await delay(50);

        // Seleciona uma posição aleatória do título
        const numchar = Math.floor(Math.random() * currentTitle.length);

        // Se já estiver corrompido, restaura o caractere original
        if (currentTitle[numchar] !== originalTitle[numchar]) {
            currentTitle[numchar] = originalTitle[numchar];
        } else {
            // Substitui pelo caractere na posição correspondente
            currentTitle[numchar] =
                titlechanges[numchar % titlechanges.length];
        }

        // Atualiza o título da página
        document.title = currentTitle.join("");
    }
})();
