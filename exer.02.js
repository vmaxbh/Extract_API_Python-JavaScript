// Importa as bibliotecas necessárias
const axios = require('axios'); // Para fazer solicitações HTTP
const fs = require('fs'); // Para manipulação de arquivos no sistema
const fse = require('fs-extra'); // Para operações avançadas de sistema de arquivos

// URL inicial para obter os dados
const url = "https://jsonplaceholder.typicode.com/posts";

// Função assíncrona para fazer a solicitação HTTP e retornar informações dos posts
async function fetchData(url) {
    try {
        // Faz uma solicitação GET para a URL fornecida
        const response = await axios.get(url);

        // Extrai os posts da resposta
        const posts = response.data;

        // Array para armazenar informações de todos os posts
        const allPosts = [];

        // Itera sobre cada post na resposta
        for (const post of posts) {
            // Cria um objeto 'info' com informações específicas do post
            const info = {
                "userID": post.userId,
                "id": post.id,
                "title": post.title,
                "body": post.body
            };

            // Exibe o ID do post no console
            console.log(post.id);

            // Adiciona o objeto 'info' ao array 'allPosts'
            allPosts.push(info);
        }

        // Não há necessidade de atualizar a URL se a API não tem paginação

        // Retorna o array com informações de todos os posts
        return allPosts;
    } catch (error) {
        // Em caso de erro na solicitação, exibe uma mensagem de erro no console
        console.error('Erro ao fazer a solicitação:', error.message);
        return null;
    }
}

// Função principal assíncrona para controlar o fluxo do programa
async function main() {
    try {
        // Define o caminho da pasta exer.02
        const folderPath = "C:\\Estudos\\Python_API_udemy\\pokemon\\exer.02";

        // Limpa todos os arquivos na pasta exer.02
        await fse.emptyDir(folderPath);

        // Chama a função fetchData para obter informações de todos os posts
        const allPosts = await fetchData(url);

        // Verifica se a obtenção de dados foi bem-sucedida
        if (allPosts) {
            // Define o caminho do arquivo onde todos os posts serão salvos
            const filePath = `${folderPath}\\all_posts.json`;

            // Escreve o array 'allPosts' em um único arquivo JSON
            fs.writeFileSync(filePath, JSON.stringify(allPosts, null, 2));

            // Exibe uma mensagem indicando que o arquivo foi salvo com sucesso
            console.log(`Salvando todos os posts em: ${filePath}`);
        }
    } catch (error) {
        console.error('Erro durante a execução do programa:', error.message);
    }
}

// Chama a função principal para iniciar a execução do programa
main();
