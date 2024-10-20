async function fetchData(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error('Dificuldade ao buscar dados da API');
    }
    return await response.json();
}