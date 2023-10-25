import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('stopwords')

print()
print("# Filtro de Promoções")
# Define as palavras que indicam Promoções
spam_words = set(['promoção', 'desconto', 'oferta', 'lançamento'])
# Define as stopwords em português
stop_words = set(stopwords.words('portuguese'))

# Instancia o analisador de sentimento
sia = SentimentIntensityAnalyzer()
# Define as três mensagens
mensagem1 = "Comunicado: LANÇAMENTO do novo Pré treino da Max!"  # Promoção de suplementtos
mensagem2 = "Coqueteleira Inox de BRINDE! Unidades limitadas!"  # Promoção, entretanto não filtrada
mensagem3 = "Receba orientações sobre IA generativa necessárias para todas as empresas"  # Treinamento AWS
# Tokeniza as mensagens
tokens1 = word_tokenize(mensagem1, language='portuguese')
tokens2 = word_tokenize(mensagem2, language='portuguese')
tokens3 = word_tokenize(mensagem3, language='portuguese')
# Remove as stopwords e converte as palavras para minúsculas
filtered1 = [w.lower() for w in tokens1 if not w in stop_words]
filtered2 = [w.lower() for w in tokens2 if not w in stop_words]
filtered3 = [w.lower() for w in tokens3 if not w in stop_words]
# Verifica se as mensagens contêm palavras indicativas de spam
if any(word in spam_words for word in filtered1) or sia.polarity_scores(mensagem1)['neg'] > \
        sia.polarity_scores(mensagem1)['pos']:
    print("Promoção!")
else:
    print("Não é promoção.")

if any(word in spam_words for word in filtered2) or sia.polarity_scores(mensagem2)['neg'] > \
        sia.polarity_scores(mensagem2)['pos']:
    print("Promoção!")
else:
    print("Não é promoção.")
if any(word in spam_words for word in filtered3) or sia.polarity_scores(mensagem3)['neg'] > \
        sia.polarity_scores(mensagem3)['pos']:
    print("Promoção!")
else:
    print("Não é promoção.")



print()
print("Filtro de email referente a vagas")

# Define as palavras que indicam Promoções
spam_words = set(['analista', 'trabalha', 'vaga', 'prova'])
# Define as stopwords em português
stop_words = set(stopwords.words('portuguese'))

# Instancia o analisador de sentimento
sia = SentimentIntensityAnalyzer()
# Define as três mensagens
mensagem1 = "'Analista de dados': Marjan Farma, Analista de Business Intelligence Jr e mais"  # Vaga
mensagem2 = "Sua viagem de quinta-feira à tarde com a Uber"  # Viagem da Uber
mensagem3 = "Cia de Talentos | Inscrição concluída com sucesso!"  # Inscrição de vaga
# Tokeniza as mensagens
tokens1 = word_tokenize(mensagem1, language='portuguese')
tokens2 = word_tokenize(mensagem2, language='portuguese')
tokens3 = word_tokenize(mensagem3, language='portuguese')
# Remove as stopwords e converte as palavras para minúsculas
filtered1 = [w.lower() for w in tokens1 if not w in stop_words]
filtered2 = [w.lower() for w in tokens2 if not w in stop_words]
filtered3 = [w.lower() for w in tokens3 if not w in stop_words]
# Verifica se as mensagens contêm palavras indicativas de spam
if any(word in spam_words for word in filtered1) or sia.polarity_scores(mensagem1)['neg'] > \
        sia.polarity_scores(mensagem1)['pos']:
    print("Vaga!")
else:
    print("Não é vaga.")

if any(word in spam_words for word in filtered2) or sia.polarity_scores(mensagem2)['neg'] > \
        sia.polarity_scores(mensagem2)['pos']:
    print("Vaga!")
else:
    print("Não é vaga.")
if any(word in spam_words for word in filtered3) or sia.polarity_scores(mensagem3)['neg'] > \
        sia.polarity_scores(mensagem3)['pos']:
    print("Vaga!")
else:
    print("Não é vaga.")


# Filtro de Cursos

print()
print("Filtro de email referente a vagas")


# Define as palavras que indicam Promoções
spam_words = set(['Cursos', 'Só Hoje', 'Pontos', 'Aproveite'])
# Define as stopwords em português
stop_words = set(stopwords.words('portuguese'))

# Instancia o analisador de sentimento
sia = SentimentIntensityAnalyzer()
# Define as três mensagens
mensagem1 = "SÓ HOJE nas lojas do Magalu! "  # Promoção Magalu
mensagem2 = "Cursos em promoção a partir de R$27,90 cada. Muita coisa pode acontecer depois de apenas um curso!"  # Curso Udemy
mensagem3 = "Três maneiras para realizar seus projetos!"  # Sugestão ADOBE
# Tokeniza as mensagens
tokens1 = word_tokenize(mensagem1, language='portuguese')
tokens2 = word_tokenize(mensagem2, language='portuguese')
tokens3 = word_tokenize(mensagem3, language='portuguese')
# Remove as stopwords e converte as palavras para minúsculas
filtered1 = [w.lower() for w in tokens1 if not w in stop_words]
filtered2 = [w.lower() for w in tokens2 if not w in stop_words]
filtered3 = [w.lower() for w in tokens3 if not w in stop_words]
# Verifica se as mensagens contêm palavras indicativas de spam
if any(word in spam_words for word in filtered1) or sia.polarity_scores(mensagem1)['neg'] > \
        sia.polarity_scores(mensagem1)['pos']:
    print("Curso!")
else:
    print("Não é curso.")

if any(word in spam_words for word in filtered2) or sia.polarity_scores(mensagem2)['neg'] > \
        sia.polarity_scores(mensagem2)['pos']:
    print("Curso!")
else:
    print("Não é curso.")
if any(word in spam_words for word in filtered3) or sia.polarity_scores(mensagem3)['neg'] > \
        sia.polarity_scores(mensagem3)['pos']:
    print("Curso!")
else:
    print("Não é curso.")
