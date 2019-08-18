from django.shortcuts import render, redirect
from  website.models import Paciente, Instituicao
from django.db.models import Q

# Create your views here.
def index(request):
    contexto= {}
    return render( request, 'index.html', contexto)

def sobre(request):
     contexto= {}
     return render( request, 'sobre.html', contexto)

# Incompleta
def agendar(request):
     # pega o valor digitado no input e filtra se tem algo parecido nas propriedades da classe Instituicao
     if request.method == 'GET':
          queryset = []
          query = request.GET.get('q')

          if not query.strip():
               print('STRING TA VAZIAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
               return render( request, 'index.html', {})

          queries = query.split(" ")

          for q in queries:
               object_list = Instituicao.objects.filter(
                    Q(nome_empresa__icontains=q) | Q(municipio__icontains=q)
               ).distinct()
               print (f'Esta é a lista de objetos {object_list} ###')

               for obj in object_list:
                    print(f'OLHA O OBJETO {obj} <<<')
                    queryset.append(obj)

          num_resultados = len(object_list)
          lista_obj = list(set(queryset))
          contexto = {'mostrar_resultados': True , 'query' : str(query), 'object_list':object_list, 'queryset':lista_obj,'num_resultados': num_resultados}
          print(contexto)
          return render( request, 'index.html', contexto)


def login(request):
    if request.method == 'POST':
     
     #Verifica se o email digitado no imput do login consta na nossa base
     email_comercical_form = request.POST.get('email')
     email_form = request.POST.get('email')
     pessoa = Paciente.objects.filter(email = email_form).first() or Instituicao.objects.filter(email_comercial = email_comercical_form).first()

     print(f'{pessoa} está tentando entrar no nosso sistema')

     # Se nada for encontrado, passar no contexto a variavel logado como false e retornar para o index, mas para o usuário
     # nao ter que clicar no botao para aparecer o modal novamente , passar a variável modal_ativo como true e fazer aconter la no html
     
     if pessoa is None: 
       print('Ops, se cadastra primeiro ai pô')
       contexto = {'msg': 'oops, não encontramos este email na nossa base de dados', 'logado':False, 'modal_ativo':True}
       return render(request, 'index.html' , contexto)
    
     # Verificar o tipo de usuário com o has attribute e retornar a variável logado como True, e mandando de volta para a  index
     else:
      if hasattr(pessoa , 'nome'):
          contexto = {'pessoa': pessoa , 'msg':f'Boas vindas, {pessoa.nome}! Aproveite o site :)','pessoa': pessoa , 'logado':True}
      elif hasattr(pessoa , 'nome_empresa'):
          contexto = {'pessoa': pessoa , 'msg':f'Boas vindas, {pessoa.nome_empresa}! Aproveite o site :)','pessoa': pessoa , 'logado':True}

      return render(request, 'index.html', contexto)

    contexto = {}
    return render( request, 'index.html', contexto)

# função de cadastrar cliente
def cadastro(request):
     contexto = {}
     if request.method == 'POST':
          paciente = Paciente()

          # checar se o email já está cadastrado
          email_digitado = request.POST.get('email')
          em_uso = Paciente.objects.filter(email = email_digitado).first()
     
          if(em_uso is None):
               paciente.nome = request.POST.get('nome')
               paciente.sobrenome = request.POST.get('sobrenome')
               paciente.data_nasc = request.POST.get('data_nasc')
               paciente.genero = request.POST.get('genero')
               paciente.cpf = request.POST.get('cpf')
               paciente.telefone= request.POST.get('telefone')
               paciente.cep = request.POST.get('cep')
               paciente.rua = request.POST.get('rua')
               paciente.complemento = request.POST.get('complemento')
               paciente.bairro = request.POST.get('bairro')
               paciente.cidade = request.POST.get('cidade')
               paciente.uf = request.POST.get('uf')
               paciente.email = request.POST.get('email')
               paciente.senha = request.POST.get('senha')
               print(paciente)
               paciente.save()
               print(paciente)
               contexto= {'msg':f'Boas vindas, {paciente.nome}! Aproveite o site :)','logado':True}
               print(f'{paciente.nome} foi cadastrado')
               return  render(request, 'index.html', contexto)

          else:
               contexto_false = {'msg':f'Parece que este email já está sendo utilizado :(', 'logado':False}
               print('error')
               return render(request, 'cadastro.html', contexto_false)
     return render(request, 'cadastro.html', contexto)

#função de cadastrar as instituições
def cadastro_instituicao(request):
     contexto={ }
     if request.method == 'POST':
          instituicao = Instituicao()
          
          email_digitado_inst = request.POST.get('email_comercial')
          em_uso_inst = Instituicao.objects.filter(email_comercial = email_digitado_inst).first()
          print('funcionou')
          
          if(em_uso_inst is None):
               print('ta funcionando')
               instituicao.nome_empresa = request.POST.get('nome_empresa')
               instituicao.email_comercial = request.POST.get('email_comercial')
               instituicao.cnpj = request.POST.get('cnpj') 
               instituicao.cep = request.POST.get('cep')
               instituicao.rua = request.POST.get('rua')
               instituicao.complemento = request.POST.get('complemento')
               instituicao.bairro = request.POST.get ('bairro')
               instituicao.uf = request.POST.get ('uf')
               instituicao.senha = request.POST.get ('senha')
               instituicao.save()
               contexto = {'instituicao': instituicao,'logado':True}
               return  render(request, 'index.html', contexto)
          else:
               contexto= {'msg':f'Ooops, parece que já cadastraram esse email'}
               return  render(request, 'cadastro.html', contexto)
     return render( request, 'index.html', contexto)

