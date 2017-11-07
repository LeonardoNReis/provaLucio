#coding: utf-8

from appJar import gui
import MySQLdb

app = gui("Crud de MySQL", "600x300")
	
#Janela Crud
def janelaLogin(btn):
	app.showSubWindow("janelaLogin")
	
	
def logar(btn):
	global cursor
	host = app.getEntry("e1")
	usuario = app.getEntry("e2")
	senha = app.getEntry("e3")
	if(host != "192.168.56.102"):
		app.errorBox("Erro","Servidor não existe!")
	if(usuario != "va1-user"):
		app.errorBox("Erro","Usuário não existe!")
	if(senha != "va1-user"):
		app.errorBox("Erro","Senha incorreta!")
	conexao = MySQLdb.connect(host, usuario, senha, "mundo")
	cursor = conexao.cursor()
	app.hideSubWindow('janelaLogin')


def pesquisar(btn):
	termo = app.getEntry("txtBusca")
	if termo == '':
		app.errorBox("Erro", 'Informe um termo para pesquisar!')
	else:
		cursor.execute("SELECT c.id, c.NomeCidade, e.NomeEstado FROM Cidade as c"+
		" INNER JOIN Estado as e ON e.id = c.idEstado"+
		" WHERE c.NomeCidade LIKE '%" + termo + "%'")
		rs = cursor.fetchall()

		app.clearListBox("lBusca")

		for x in rs:
			app.addListItem("lBusca", str(x[0]) + ' - ' + x[1] + ' - ' + x[2])


def pais(btn):
	pais = app.textBox("Inserir Pais", "Digite o nome do Pais: ", parent=None)
	if pais == '':
		app.errorBox("Erro", 'Informe um termo para pesquisar!')
	else:
		cursor.execute("INSERT INTO Pais (NomePais) VALUES ('"+ pais +"')")
		conexao.commit()	
	
	
def estado(btn):
	app.showSubWindow("janelaEstado")

def cidade(btn):
	app.showSubWindow("janelaCidade")

def insert(btn):
	app.showSubWindow("janelaInsert")



## UPDATE
def update(btn):
	app.showSubWindow("janelaUpdate")
	
def paisUpdate(btn):
	app.showSubWindow("janelaPaisUpdate")
	
def estadoUpdate(btn):
	app.showSubWindow("janelaEstadoUpdate")
	
def cidadeUpdate(btn):
	app.showSubWindow("janelaCidadeUpdate")


## DELETE
def delete(btn):
	app.showSubWindow("janelaCidadeDelete")

#Delete Cidade
def deletarCidade(btn):
	##nomeCidade = app.getEntry('txtNomeCidade')
	idCidade = app.getEntry('txtIdDeleteCidade')
	cursor.execute("DELETE FROM Cidade WHERE id = " + idCidade)
	conexao.commit()
	app.hideSubWindow('janelaCidadeDelete')


#Janela de Cidade para Insert
app.startSubWindow("janelaCidadeDelete", modal=True)
app.addLabel("l8", "Deletando Cidades")
app.addEntry('txtIdDeleteCidade')
app.addButton('Deletar cidade', deletarCidade)
#app.setEntryDefault("txtNomeCidade", "Digite o Nome da Cidade")
app.setEntryDefault("txtIdDeleteCidade", "Digite o ID da Cidade")
app.stopSubWindow()



#Insert Estado
def salvarEstado(btn):
	nomeEstado = app.getEntry('txtNomeEstado')
	idPais = app.getEntry('txtIdPais')	
	cursor.execute("INSERT INTO Estado (NomeEstado, idPais) VALUES('{}',{})".format(nomeEstado, idPais))
	conexao.commit()
	app.hideSubWindow('janelaEstado')
	
#Insert Cidade
def salvarCidade(btn):
	nomeCidade = app.getEntry('txtNomeCidade')
	idEstado = app.getEntry('txtIdEstado')
	cursor.execute("INSERT INTO Cidade (NomeCidade, idEstado) VALUES('{}',{})".format(nomeCidade, idEstado))
	conexao.commit()
	app.hideSubWindow('janelaCidade')


#Janela de Cidade para Insert
app.startSubWindow("janelaCidade", modal=True)
app.addLabel("l3", "Inserindo dados de Cidade")
app.addEntry('txtNomeCidade')
app.addEntry('txtIdEstado')
app.addButton('Salvar cidade',salvarCidade)
app.setEntryDefault("txtNomeCidade", "Digite o Nome da Cidade")
app.setEntryDefault("txtIdEstado", "Digite o ID do Estado")
app.stopSubWindow()

#Janela de Estado para insert
app.startSubWindow("janelaEstado", modal=True)
app.addLabel("l2", "Inserindo dados de Estado")
app.addEntry('txtNomeEstado')
app.addEntry('txtIdPais')
app.addButton('Salvar estado',salvarEstado)
app.setEntryDefault("txtNomeEstado", "Digite o Nome do Estado")
app.setEntryDefault("txtIdPais", "Digite o ID do Pais")
app.stopSubWindow()



#Janela Insert para poder escolher qual será a inserção	
app.startSubWindow("janelaInsert", modal=True)
app.addLabel("l1", "Inserindo dados...")
app.addButton("Pais", pais, 1,0)
app.addButton("Estado", estado, 0,1)
app.addButton("Cidade", cidade, 1,1)
app.stopSubWindow()


#Update Pais
def alterarPais(btn):
	nomePais = app.getEntry('txtNomeUpdatePais')
	idPais = app.getEntry('txtIdUpdatePais')
	cursor.execute("UPDATE Pais SET NomePais = '"+ nomePais +"' WHERE id = "+ idPais)
	conexao.commit()
	app.hideSubWindow('janelaPaisUpdate')


#Update Cidade
def alterarCidade(btn):
	nomeCidade = app.getEntry('txtNomeUpdateCidade')
	idCidade = app.getEntry('txtIdUpdateCidade')
	cursor.execute("UPDATE Cidade SET NomeCidade = '"+ nomeCidade +"' WHERE id = "+ idCidade)
	conexao.commit()
	app.hideSubWindow('janelaEstadoUpdate')


#Update Estado
def alterarEstado(btn):
	nomeEstado = app.getEntry('txtNomeUpdateEstado')
	idEstado = app.getEntry('txtIdUpdateEstado')
	cursor.execute("UPDATE Estado SET NomeEstado = '"+ nomeEstado +"' WHERE id = "+ idEstado)
	conexao.commit()
	app.hideSubWindow('janelaEstadoUpdate')


#Janela Update para poder escolher qual será a atualização	
app.startSubWindow("janelaUpdate", modal=True)
app.addLabel("l4", "Atualizando dados...")
app.addButton("alterarPais", paisUpdate, 1,0)
app.addButton("alterarEstado", estadoUpdate, 0,1)
app.addButton("alterarCidade", cidadeUpdate, 1,1)
app.stopSubWindow()



#Janela de Pais para Update
app.startSubWindow("janelaPaisUpdate", modal=True)
app.addLabel("l7", "Alterar Nome do Pais")
app.addEntry('txtNomeUpdatePais')
app.addEntry('txtIdUpdatePais')
app.addButton('Alterar Pais', alterarPais)
app.setEntryDefault("txtNomeUpdatePais", "Digite o Nome do Pais")
app.setEntryDefault("txtIdUpdatePais", "Digite o ID do Pais")
app.stopSubWindow()


#Janela de Cidade para Update
app.startSubWindow("janelaCidadeUpdate", modal=True)
app.addLabel("l5", "Alterar Nome da Cidade")
app.addEntry('txtNomeUpdateCidade')
app.addEntry('txtIdUpdateCidade')
app.addButton('Alterar cidade', alterarCidade)
app.setEntryDefault("txtNomeUpdateCidade", "Digite o Nome da Cidade")
app.setEntryDefault("txtIdUpdateCidade", "Digite o ID da Cidade")
app.stopSubWindow()


#Janela de Estado para Update
app.startSubWindow("janelaEstadoUpdate", modal=True)
app.addLabel("l6", "Alterar Nome do Estado")
app.addEntry('txtNomeUpdateEstado')
app.addEntry('txtIdUpdateEstado')
app.addButton('Alterar estado', alterarEstado)
app.setEntryDefault("txtNomeUpdateEstado", "Digite o Nome do Estado")
app.setEntryDefault("txtIdUpdateEstado", "Digite o ID do Estado")
app.stopSubWindow()



## Menu Principal
app.addLabel("lNome", '', 0,0,2)
app.addButton("Fazer Login", janelaLogin, 1,0)
app.addButton("Inserir dado", insert, 1,1)
app.addButton("Atualizar dado", update, 2,0)
app.addButton("Excluir dado", delete, 2,1)
app.addEntry("txtBusca", 3,0,2)
app.setEntryDefault("txtBusca", "Digite a Cidade que busca...")
app.addButton("Pesquisar", pesquisar, 4,0,2)
app.addListBox("lBusca", [], 5,0,2)
app.setListBoxRows("lBusca", 5)



# Tela de Login
app.startSubWindow("janelaLogin", modal=True)
app.addLabel("l10", "Fazer Login")
app.addEntry('e1')
app.addEntry('e2')
app.addEntry('e3')
app.setEntryDefault("e1", "Host")
app.setEntryDefault("e2", "Usuario")
app.setEntryDefault("e3", "Senha")
app.addButton("Logar", logar)

app.stopSubWindow()



app.go()
