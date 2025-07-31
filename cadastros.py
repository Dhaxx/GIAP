import conexao as cnx

cur_origem = cnx.cur
cur_destino = cnx.cur_d
EMPRESA = 1

def tipos_de_bens():
    print("CADASTRO DE TIPOS")

    try:
        cur_destino.execute('alter table pt_cadtip add CODANT varchar(10)')
        cnx.commit()
    except:
        pass

    cur_destino.execute("delete from pt_cadtip")
    insert = cur_destino.prep("""insert into pt_cadtip(codigo_tip, empresa_tip, descricao_tip, codant) values (?,?,?,?)""")
    cur_origem.execute("select * from pm_especie")

    for i, row in enumerate(cur_origem):
        i += 1
        codigo_tip = i
        empresa_tip = EMPRESA
        descricao_tip = row[2]
        codant = row[0]
        cur_destino.execute(insert,(codigo_tip,empresa_tip,descricao_tip,codant))
    cnx.commit()

def grupos_de_bens():
    print("INSERINDO GRUPOS...")

    try:
        cur_destino.execute('alter table pt_cadpatg add CODANT varchar(10)')
        cnx.commit()
    except:
        pass

    cur_destino.execute("delete from pt_cadpatg")
    insert = cur_destino.prep("insert into pt_cadpatg(codigo_gru,empresa_gru,nogru_gru,codant) values(?,?,?,?)")
    cur_origem.execute("select * from import_tipo_patr")

    for codigo_gru, row in enumerate(cur_origem):
        codigo_gru += 1
        empresa_gru = EMPRESA
        nogru_gru = row[1]
        codant = row[0]
        cur_destino.execute(insert,(codigo_gru,empresa_gru,nogru_gru,codant))
    cnx.commit()
        
def situacoes():
    print("INSERINDO SITUAÇÕES...")

    cur_destino.execute("delete from pt_cadsit")
    insert = cur_destino.prep("insert into pt_cadsit (codigo_sit, empresa_sit, descricao_sit) values (?,?,?)")
    cur_origem.execute("""SELECT * FROM pm_tipo_conservacao""")

    for row in cur_origem:
        codigo_sit = int(row[0])
        empresa_sit = EMPRESA
        descricao_sit = row[1]

        cur_destino.execute(insert,(codigo_sit, empresa_sit, descricao_sit))
    cnx.commit()

def unidades():
    print("INSERINDO UNIDADES...")
    dados = [(1, 'GABINETE', 'MATHEUS AUGUSTO VENANCIO'),
    (10, 'SECRETARIA DE TURISMO, CULTURA E DESENVOLVIMENTO ECONOMICO', 'CAROLINA RIBEIRO SILVA'),
    (11, 'SECRETARIA DE SAÚDE E SANEAMENTO', 'ADRIELLE ALINE COSTA TEIXEIRA'),
    (12, 'SECRETARIA DE CIDADANIA', 'SUELY DIAS VENANCIO COSTA'),
    (13, 'SECRETARIA DE FAZENDA', 'MARILENE APARECIDA DOS SANTOS'),
    (14, 'FDCA', 'RONALDO RIVELINO VENANCIO'),
    (15, 'CRAS', 'RONALDO RIVELINO VENANCIO'),
    (16, 'MERENDA ESCOLAR', 'AURORA MARIGILDA DA ROSA SANTOS'),
    (17, 'SERVIÇO DE ESTRADA DE RODAGEM', 'RONALDO RIVELINO VENANCIO'),
    (18, 'SERVIÇOS MUNICIPAIS', 'RONALDO RIVELINO VENANCIO'),
    (19, 'SECRETARIA DE INFRAESTRUTURA, SEGURANÇA E MOBILIDADE', 'ARETHUSA APARECIDA DOS SANTOS'),
    (2, 'SECRETARIA DE GOVERNO E ADMINISTRAÇÃO', 'MATHEUS AUGUSTO VENANCIO'),
    (20, 'SECRETARIA DE TURISMO', 'MATHEUS AUGUSTO VENANCIO'),
    (21, 'DEPARTAMENTO DE ESPORTES E LAZER', 'FABIO LUIZ DOS SANTOS SILVA'),
    (22, 'DEPARTAMENTO DE CULTURA', 'CAROLINA RIBEIRO SILVA'),
    (23, 'SERVIÇO DE GESTÃO TRIBUTÁRIA', ''),
    (24, 'DEPARTAMENTO DE COMPRAS E LICITAÇÕES', 'MATHEUS AUGUSTO VENANCIO'),
    (25, 'ALMOXARIFADO DA FARMÁCIA', 'ADRIELLE ALINE COSTA TEIXEIRA'),
    (26, 'ALMOXARIFADO CENTRAL', 'MATHEUS AUGUSTO VENANCIO'),
    (27, 'DEPARTAMENTO DE SERVIÇOS PÚBLICOS E ZELADORIA', 'FLAVIO APARECIDO DA SILVA'),
    (28, 'SECRETARIA DE TURISMO E DESENVOLVIMENTO ECONÔMICO', 'MATHEUS AUGUSTO VENANCIO'),
    (29, 'SECRETARIA DA FAZENDA', ''),
    (3, 'SECRETARIA DE FINANÇAS E ORÇAMENTO', 'MATHEUS AUGUSTO VENANCIO'),
    (30, 'SECRETARIA DE AGRICULTURA E MEIO AMBIENTE', 'RAFAEL OLIMPIO SILVA'),
    (31, 'SECRETARIA DE EDUCAÇÃO', 'JOAO PEDRO VENANCIO DA ROSA'),
    (32, 'ALMOXARIFADO MERENDA', 'AURORA MARIGILDA DA ROSA SANTOS'),
    (33, 'ALMOXARIFADO EDUCAÇÃO', 'AURORA MARIGILDA DA ROSA SANTOS'),
    (34, 'POSTO DE SAÚDE', 'ADRIELLE ALINE COSTA TEIXEIRA'),
    (35, 'Compras Notas Fiscais', 'MATHEUS AUGUSTO VENANCIO'),
    (36, 'SETOR DE PROMOÇÃO ESPORTES COMUNITÁRIOS RECREAÇÃO', 'FABIO LUIZ DOS SANTOS SILVA'),
    (37, 'SETOR DE FOMENTO DA CULTURA', 'MATHEUS AUGUSTO VENANCIO'),
    (38, 'SETOR DE ADMINISTRAÇÃO GERAL', 'MATHEUS AUGUSTO VENANCIO'),
    (39, 'FUNDO MUNICIPAL DE ASSISTÊNCIA SOCIAL', 'RONALDO RIVELINO VENANCIO'),
    (4, 'ADMINISTRAÇÃO E COORDENAÇÃO', 'MATHEUS AUGUSTO VENANCIO'),
    (40, 'GABINETE DO PREFEITO', 'MATHEUS AUGUSTO VENANCIO'),
    (41, 'FUNDO MUNICIPAL DE SAÚDE', 'ADRIELLE ALINE COSTA TEIXEIRA'),
    (42, 'SETOR DE SERVIÇOS URBANOS', 'RONALDO RIVELINO VENANCIO'),
    (43, 'SETOR DE ABASTECIMENTO E EXTENSÃO RURAL', 'RONALDO RIVELINO VENANCIO'),
    (44, 'SETOR DE INCREMENTO DO TURISMO', 'RONALDO RIVELINO VENANCIO'),
    (45, 'SERM E OFICINAS', 'RONALDO RIVELINO VENANCIO'),
    (46, 'SETOR DE ARRECADAÇÃO TRIBUTÁRIA', ''),
    (47, 'FUNDO SOCIAL DE SOLIDARIEDADE', 'RONALDO RIVELINO VENANCIO'),
    (48, 'CONSELHO TUTELAR', 'SUELY DIAS VENANCIO COSTA'),
    (49, 'SECRETARIA DE PLANEJAMENTO, CONVENIOS E ASSUNTOS ESTRATÉGICOS', 'RAFAEL BARBOSA DE AGUIAR'),
    (5, 'SETOR DE FINANÇAS', 'MATHEUS AUGUSTO VENANCIO'),
    (50, 'DEPARTAMENTO DE SEGURANÇA PÚBLICA E DEFESA CIVIL', 'ARETHUSA APARECIDA DOS SANTOS'),
    (51, 'ALMOXARIFADO AUTOMOTIVO', 'WESLEY YAGO DA SILVA ROSA'),
    (52, 'ALMOXARIFADO LIMPEZA EDUCAÇÃO', 'AURORA MARIGILDA DA ROSA SANTOS'),
    (6, 'ENSINO FUNDAMENTAL', 'AURORA MARIGILDA DA ROSA SANTOS'),
    (7, 'SECRETARIA DE SERVIÇOS PUBLICOS E ZELADORIA', 'FLAVIO APARECIDO DA SILVA'),
    (8, 'ENSINO INFANTIL', 'AURORA MARIGILDA DA ROSA SANTOS'),
    (9, 'SECRETARIA DE AGRICULTURA E MEIO AMBIENTE', 'FABIO LUIZ DOS SANTOS SILVA')]

    insert = cur_destino.prep("insert into pt_cadpatd(codigo_des, empresa_des, nauni_des, responsa_des) values (?,?,?,?)")
    
    for row in dados:
        print(row)
        codigo_des = row[0]
        empresa_des = EMPRESA
        nauni_des = row[1]
        responsa_des = row[2]
        cur_destino.execute(insert,(codigo_des,empresa_des, nauni_des[:60],responsa_des))
    cnx.commit()

def subunidades():
    print("INSERINDO SUBUNIDADES...")

    try:
        cur_destino.execute('alter table pt_cadpats add CODANT varchar(10)')
        cnx.commit()
    except:
        pass

    dados = [(12, 25, 'CONSELHO TUTELAR'),
    (15, 14, 'BOLSA FAMILIA'),
    (15, 21, 'CENTRO DE REFERENCIA DE ASSISTENCIA SOCIAL'),
    (18, 106, 'OBRAS'),
    (18, 120, 'ACADEMIA AO AR LIVRE - BAIRRO QUILOMBO'),
    (18, 127, 'ACADEMIA AO AR LIVRE - BAIRRO BAU'),
    (18, 128, 'ACADEMIA AO AR LIVRE - BAIRRO CANTAGALO'),
    (18, 129, 'ACADEMIA AO AR LIVRE - BAIRRO SERRANO'),
    (18, 130, 'ACADEMIA AO AR LIVRE - BAIRRO PINHEIRO'),
    (18, 135, 'PARQUINHO MUNICIPAL - RANCHO FUNDO'),
    (18, 136, 'PARQUINHO MUNICIPAL - NOVA CONQUISTA'),
    (18, 158, 'SALA DO ELETRICISTA'),
    (18, 16, 'CASA DE MAQUINAS DA PRACA GEN. MARCONDES'),
    (18, 160, 'ACADEMIA AO AR LIVRE - BAIRRO PAIOL GRANDE'),
    (18, 164, 'ACADEMIA AO AR LIVRE CENTRO'),
    (18, 18, 'CEMITERIO MUNICIPAL'),
    (18, 29, 'COZINHA SECRETARIA DE OBRAS'),
    (18, 63, 'LAVADOR DE CARROS - BLOQUETE'),
    (18, 65, 'Oficina de Marcenaria'),
    (18, 66, 'OFICINA MECANICA'),
    (18, 67, 'PARQUINHO BAIRRO DO QUILOMBO'),
    (18, 68, 'PARQUINHO MUNICIPAL - CENTRO'),
    (18, 69, 'PATIO PAÇO MUNICIPAL'),
    (18, 84, 'SALA DA JARDINAGEM'),
    (18, 99, 'SECRETARIA DE OBRAS E SERVICOS MUNICIPAIS'),
    (19, 32, 'DEFESA CIVIL'),
    (19, 33, 'ENGENHARIA E OBRAS'),
    (2, 104, 'COMPRAS'),
    (2, 166, 'Sub - Secretaria'),
    (2, 28, 'CORREDOR ÁREA DE SERVIÇO'),
    (2, 95, 'Secretaria de Administração'),
    (26, 3, 'ALMOXARIFADO CENTRAL'),
    (29, 35, 'DPTO DE CADASTRO E TRIBUTACAO'),
    (3, 26, 'CONTABILIDADE'),
    (3, 57, 'FINANCAS E ORCAMENTO'),
    (30, 134, 'MONA - CENTRO DE VISITANTE'),
    (30, 165, 'ECOPONTO'),
    (30, 23, 'CENTRO DE TRIAGEM DE RESIDUOS SOLIDOS'),
    (30, 64, 'Mona - Monumento Natural Pedra do Baú'),
    (30, 91, 'SECRETARIA DE AGRICULTURA E MEIO AMBIENTE'),
    (34, 22, 'CENTRO DE SAUDE'),
    (36, 163, 'ACADEMIA AO AR LIVRE CENTRO ESPORTIVO'),
    (36, 20, 'CENTRO DE LAZER DO TRABALHADOR'),
    (36, 55, 'ESTADIO MUNICIPAL BENEDITO GOMES DE SOUZA'),
    (36, 98, 'Secretaria de Esportes e Lazer'),
    (37, 124, 'ESPACO BAMASB'),
    (37, 126, 'MUSEU DO ZE PEREIRA'),
    (37, 13, 'BIBL. MUNIC. Mª. ASTROGILDA DE ASSIS CAMARGO'),
    (37, 34, 'DIRETORIA DE CULTURA E EVENTOS'),
    (37, 71, 'TORRES - PORTAL'),
    (38, 103, 'SECRETARIA GERAL DE ASSUNTOS JURIDICOS'),
    (38, 104, 'COMPRAS'),
    (38, 105, 'LICITACAO'),
    (38, 107, 'PATRIMONIO/JUNTA MILITAR'),
    (38, 108, 'TRANSPORTE MUNICIPAL'),
    (38, 121, 'CORREDORES'),
    (38, 161, 'SINDICÂNCIA'),
    (38, 166, 'Sub - Secretaria'),
    (38, 27, 'CONTROLE INTERNO'),
    (38, 28, 'CORREDOR ÁREA DE SERVIÇO'),
    (38, 3, 'ALMOXARIFADO CENTRAL'),
    (38, 30, 'COZINHA E ÁREA DE SERVIÇO ADMINISTRAÇÃO'),
    (38, 31, 'CPD - CENTRAL DE PROCESSAMENTO DE DADOS'),
    (38, 33, 'ENGENHARIA E OBRAS'),
    (38, 37, 'DEPARTAMENTO DE INFORMATICA'),
    (38, 38, 'SEGURANCA DO TRABALHO'),
    (38, 39, 'DEPARTAMENTO PESSOAL'),
    (38, 4, 'ALMOXARIFADO LIMPEZ'),
    (38, 59, 'GUARITA/JARDIM DO PACO'),
    (38, 60, 'INSS - FAZENDA'),
    (38, 61, 'Jardim do Paço Municipal'),
    (38, 8, 'ARQUIVO'),
    (38, 80, 'PROCURADORIA'),
    (38, 83, 'RECEPCAO'),
    (38, 87, 'SALA DE COPIAS'),
    (38, 89, 'SALA DE REUNIAO'),
    (38, 9, 'AUDITORIO'),
    (38, 94, 'SECRETARIA PROTOCOLO'),
    (38, 95, 'Secretaria de Administração'),
    (38, 156, 'SALA DE ATENDIMENTO'),
    (38, 157, 'SALA DE REUNIOES'),
    (38, 96, 'SECRETARIA DE DESENVOLVIMENTO DE ASSISTENCIA SOCIA'),
    (39, 96, 'SECRETARIA DE DESENVOLVIMENTO DE ASSISTENCIA SOCIA'),
    (39, 156, 'SALA DE ATENDIMENTO'),
    (39, 157, 'SALA DE REUNIOES'),
    (40, 58, 'GABINETE DO PREFEITO'),
    (40, 62, 'Junta Militar'),
    (40, 90, 'Sala do Chefe de Gabinete'),
    (40, 25, 'Conselho Tutelar'),
    (40, 32, 'DEFESA CIVIL'),
    (40, 102, 'Secretaria do Fundo municipal de Solidariedade - Paço Municipal'),
    (41, 101, 'SECRETARIA DE SAUDE E SANEAMENTO'),
    (41, 110, 'VIGILANCIA EPIDEMIOLOGICA'),
    (41, 111, 'VIGILANCIA SANITARIA'),
    (41, 144, 'DEPOSITO SAUDE - MERCADO MUNICIPAL'),
    (41, 145, 'ESTRATEGIA SAUDE DA FAMILIA'),
    (41, 146, 'FARMACIA'),
    (41, 148, 'POSTO DE SAUDE - PINHEIROS'),
    (41, 149, 'VIVA LEITE'),
    (41, 162, 'POSTO DE SAUDE PAIOL'),
    (41, 19, 'CENTRAL DE VAGAS'),
    (41, 22, 'CENTRO DE SAUDE'),
    (41, 73, 'POSTO DE SAUDE - BAU'),
    (41, 74, 'POSTO DE SAUDE - BOCAINA'),
    (41, 75, 'POSTO DE SAUDE - CANTAGALO'),
    (41, 76, 'POSTO DE SAUDE - JOSE DA ROSA (PAIOL VELHO)'),
    (41, 77, 'POSTO DE SAUDE - QUILOMBO'),
    (41, 78, 'POSTO DE SAUDE - SERRANOS'),
    (41, 79, 'POSTO DE SAUDE - TORTO'),
    (41, 88, 'SALA DE FISIOTERAPIA'),
    (44, 10, 'BANCO DO POVO PAULISTA'),
    (44, 54, 'ESPACO DO EMPREENDEDOR'),
    (44, 71, 'TORRES - PORTAL'),
    (44, 72, 'Portal - Torre 2'),
    (44, 86, 'Sala de Assessoria'),
    (44, 92, 'SECRET. TURISMO E DESENV. ECONOMICO'),
    (44, 93, 'Secret. Turismo: Corredores Copa e Depósito'),
    (46, 131, 'FISCAL DE OBRAS E POSTURA MUNICIPAL'),
    (46, 155, 'INCRA'),
    (46, 35, 'DPTO DE CADASTRO E TRIBUTACAO'),
    (47, 51, 'ESCOLA DA BELEZA'),
    (47, 52, 'Escola de Beleza (maquiagem)'),
    (47, 82, 'PROJETO COSTURANDO SAO BENTO DO SAPUCAI'),
    (49, 100, 'SECRETARIA DE PLANEJAMENTO E GESTAO'),
    (5, 109, 'TESOURARIA'),
    (5, 26, 'CONTABILIDADE'),
    (5, 57, 'FINANCAS E ORCAMENTO'),
    (6, 123, 'SALA NUTRICIONISTA'),
    (6, 138, 'Ponto de Ônibus Bairro Paiol Grande')
    (6, 122, 'SALA DOS MOTORISTAS'),
    (6, 132, 'PONTOS DE ONIBUS'),
    (6, 143, 'Almoxarifado Central - Sala de estoque de produto de limpeza'),
    (6, 2, 'AEE - CORONEL'),
    (6, 40, 'EMEF BAIRRO DO BAU'),
    (6, 41, 'EMEF BAIRRO CANTAGALO'),
    (6, 42, 'EMEF (R) Bairro do Paiol Grande (desativada)'),
    (6, 43, 'EMEF BAIRRO DO QUILOMBO'),
    (6, 44, 'EMEF BAIRRO DO SERRANOS'),
    (6, 46, 'EMEF BAIRRO TORTO'),
    (6, 48, 'EMEF FUNDACAO PAIOL GRANDE'),
    (6, 49, 'EMEF CEL. RIBEIRO DA LUZ'),
    (6, 5, 'ALMOXARIFADO - SALA DA MERENDA'),
    (6, 6, 'Almoxarifado da Educação - Galpão'),
    (6, 63, 'LAVADOR DE CARROS - BLOQUETE'),
    (6, 81, 'PROJETO CERAMICA JOAO DE BARRO'),
    (6, 97, 'SECRETARIA DE EDUCACAO - PACO MUNICIPAL'),
    (8, 125, 'CRECHE DO QUILOMBO'),
    (8, 17, 'CEMEI MARIA CLEISON MENDES ROBERT'),
    (8, 45, 'EMEF BAIRRO DO SITIO'),
    (10, 169, 'ESPAÇO CULTURAL MUNICIPAL')
]

    cur_destino.execute("delete from pt_cadpats")
    insert = cur_destino.prep("insert into pt_cadpats(codigo_set,empresa_set,codigo_des_set, noset_set, ocultar_set, codant) values (?,?,?,?,?,?)")

    for  row in enumerate(dados):   
        codigo_set = str(row[1][0]) + str(row[1][1])
        empresa_set = EMPRESA
        codigo_des_set = row[1][0]
        noset_set = row[1][2]
        ocultar_set = 'N'
        codant = row[1][0]
        cur_destino.execute(insert,(codigo_set,empresa_set,codigo_des_set,noset_set,ocultar_set,codant))
    cnx.commit()
       
def tipo_baixas():
    print('INSERINDO TIPOS DE BAIXAS...')

    cur_destino.execute('delete from pt_cadbai')
    insert = cur_destino.prep("insert into pt_cadbai(codigo_bai, empresa_bai, descricao_bai) values (?,?,?)")
    tipos = [(1, EMPRESA, 'BAIXA'),
             (2, EMPRESA, 'BAIXA SOB LEVANTAMENTO PATRIMONIAL'),
             (3, EMPRESA, 'INSERVÍVEL'),
             (4, EMPRESA, 'DESINCORPORAÇÃO')]

    cur_destino.executemany(insert, tipos)
    cnx.commit()

def responsa():
    print("Iserindo Responsáveis...")

    insert = cur_destino.prep("insert into pt_cadresponsavel(codigo_resp, nome_resp) values (?,?)")
    cur_origem.execute("""SELECT * FROM import_responsaveis""")

    for row in cur_origem.fetchall():
        cur_destino.execute(insert,(int(row[0]),row[1]))
    cnx.commit()