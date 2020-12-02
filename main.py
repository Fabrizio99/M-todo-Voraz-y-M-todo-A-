# Método voraz

class Nodo:
    def __init__(self, origen, final,distancia):
        self.origen    = origen
        self.final     = final
        self.distancia = distancia

class NodoElegido:
    def __init__(self, punto, distancia,dlr):
        self.punto     = punto
        self.distancia = distancia
        self.dlr       = dlr
grafo = []
grafo.append(Nodo('Oradea'        , 'Zerind'        , 71 ))
grafo.append(Nodo('Oradea'        , 'Sibiu'         , 151))
grafo.append(Nodo('Zerind'        , 'Arad'         , 75 ))
grafo.append(Nodo('Arad'          , 'Sibiu'         , 140))
grafo.append(Nodo('Arad'          , 'Timisoara'     , 118))
grafo.append(Nodo('Sibiu'         , 'Fagaras'       , 99 ))
grafo.append(Nodo('Fagaras'       , 'Bucharest'     , 211))
grafo.append(Nodo('Timisoara'     , 'lugoj'         , 111))
grafo.append(Nodo('Lugoj'         , 'Mehadia'       , 70 ))
grafo.append(Nodo('Mehadia'       , 'Dobreta'       , 75 ))
grafo.append(Nodo('Dobreta'       , 'Craiova'       , 120))
grafo.append(Nodo('Craiova'       , 'RimnicuVilcea', 146))
grafo.append(Nodo('Craiova'       , 'Pitesti'       , 138))
grafo.append(Nodo('RimnicuVilcea' , 'Sibiu'         , 80 ))
grafo.append(Nodo('RimnicuVilcea' , 'Pitesti'       , 97 ))
grafo.append(Nodo('Pitesti'       , 'Bucharest'     , 101))
grafo.append(Nodo('Bucharest'     , 'Giurgiu'       , 90 ))
grafo.append(Nodo('Bucharest'     , 'Uziceni'       , 85 ))
grafo.append(Nodo('Uziceni'       , 'Hirsova'       , 98 ))
grafo.append(Nodo('Hirsova'       , 'Eforie'        , 86 ))
grafo.append(Nodo('Uziceni'       , 'Vaslui'        , 142))
grafo.append(Nodo('Vaslui'        , 'Iasi'          , 92 ))
grafo.append(Nodo('Iasi'          , 'Neamt'         , 87 ))


heuristica = {}
heuristica['Arad']      = 366
heuristica['Bucharest']  = 0
heuristica['Craiova']   = 160
heuristica['Dobreta']   = 242
heuristica['Efoire']    = 161
heuristica['Fagaras']   = 178
heuristica['Giurgiu']   = 77
heuristica['Hirsova']   = 151
heuristica['Iasi']      = 226
heuristica['Lugoj']     = 244
heuristica['Mehadia']   = 241
heuristica['Neamt']     = 234
heuristica['Oradea']    = 380
heuristica['RimnicuVilcea'] = 193
heuristica['Vilcea']    = 193
heuristica['Sibiu']     = 253
heuristica['Timisoara'] = 329
heuristica['Urziceni']  = 80
heuristica['Vaslui']    = 199
heuristica['Zerind']    = 374
heuristica['Pitesti']   = 98

rutaFinal = []
rutaAsteriscoFinal = []
acumulador = 0


def hallarVorazMenor(origen,destino):

  if destino == origen:
    return

  caminosPosibles = [ruta for ruta in grafo if ruta.origen == origen or ruta.final == origen]
  candidatos = []
  for i in range(len(caminosPosibles)):
    posible = caminosPosibles[i].origen if caminosPosibles[i].final == origen else caminosPosibles[i].final

    candidatos.append(NodoElegido(posible,caminosPosibles[i].distancia,heuristica[posible]))


  candidatos.sort(key=lambda x:x.dlr)
  rutaFinal.append(candidatos[0])

  hallarVorazMenor(candidatos[0].punto,destino)

def hallarAsteriscoMenor(origen,destino):
  global acumulador
  if destino == origen:
    return

  caminosPosibles = [ruta for ruta in grafo if ruta.origen == origen or ruta.final == origen]
  candidatos = []
  for i in range(len(caminosPosibles)):
    posible = caminosPosibles[i].origen if caminosPosibles[i].final == origen else caminosPosibles[i].final

    candidatos.append(NodoElegido(posible,caminosPosibles[i].distancia,heuristica[posible]))

  candidatos.sort(key=lambda x:x.dlr+x.distancia+acumulador)

  rutaAsteriscoFinal.append(candidatos[0])
  acumulador = acumulador + (candidatos[0].distancia)

  hallarAsteriscoMenor(candidatos[0].punto,destino)

def metodoVoraz(origen,destino):
  hallarVorazMenor(origen,destino)
  
  ruta = origen
  costoTotal = 0

  for i in range(len(rutaFinal)):
    ruta+=('-'+rutaFinal[i].punto)
    costoTotal+=rutaFinal[i].distancia

  print('METODO VORAZ')
  print('RUTA')
  print(ruta)
  print('TOTAL')
  print(costoTotal)
    
def metodoAsterisco(origen,destino):
  hallarAsteriscoMenor(origen,destino)
  ruta = origen

  for i in range(len(rutaAsteriscoFinal)):
    ruta+=('-'+rutaAsteriscoFinal[i].punto)

  print('METODO A*')
  print('RUTA')
  print(ruta)





metodoVoraz('Arad','Bucharest')
print('')
metodoAsterisco('Arad','Bucharest')