# Graph(Map) Coloring project
from queue import Empty, PriorityQueue as pq    # Degree Heuristic kullanabilmek icin priority Queue kutuphanesini import ettim.
class Vertex:                                   # Sehirleri dugum olarak hafizaya yazmak icin vertex sinifi olusturdum.
    def __init__(self, node):                   # Vertex sinifinin her bir elemanina eklenecek ozellikleri __init__ fonksiyonunda tanimladim.
        self.id = node                          # Her bir dugum icin id atamasi yaptim.
        self.color = None                       # Her bir sehirin aldigi rengi tutacak color degiskeni olusturdum ve None olarak atama yaptim.
        self.posibility = []                    # Her bir sehir icin alabilecegi domainleri tutan posibility listesini olusturdum.
        self.adjacent = {}                      # Her bir dugumun komsularini tutabilmek icin komsuluk listesi olusturdum.

    def __str__(self):                          # Her bir sehrin komsuluk iliskilerini yazdirmak icin __str__ fonksiyonu olusturdum.
        return str(self.id) + ' Sehrinin Komsuları: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0): # Dugumlere komsu ekleyebilmek icin fonksiyon olusturdum ve fonksiyon girdisi olarak iki komsu sehiri ve aralarindaki ulasim mesafesini aldim.
        self.adjacent[neighbor] = weight
    
    def get_neighbors(self):                    # Dugumlerin komsularina erisebilmek icin fonksiyon yazdim.
        return [x.id for x in self.adjacent]

    def get_connections(self):                  # Dugumler arasindaki bahlantilari donduren fonksiyonu yazdim.
        return self.adjacent.keys()

    def get_id(self):                           # Dugumlerin id' lerine ulasabilmek icin fonksiyon olusturdum.
        return self.id

    def get_NeighborCount(self):                # Derece Heuristiginde kullanilacak olan komsu sehir sayisini donduren get_NeighborCount fonksionunu yazdim.
        return len(self.adjacent)
        

class Graph:                                    # Dugumlerin komsuluk yapisini olusturabilmek icin Graph sinifini olusturdum.
    def __init__(self):
        self.vert_dict = {}                     # Dugumlerin kolsularini listeleyebilmek icin vert_dict listesini olusturdum.
        self.num_vertices = 0                   # Her bir dugumun kac tane komsusu oldugunu tutacak degiskeni atadim.

    def __iter__(self):                         # Dugumun komsularini fonksiyon ciktisi olarak dondurecek __iter__ fonksiyonunu olusturdum.
        return iter(self.vert_dict.values())

    def add_vertex(self, node):                 # Yeni dugum ekleyebilmek icin add_vertex() fonksiyonunu olusturdum ve parametre olarak dugumun ismini aldim.
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)               # Vertex sinifindan yeni bir vertex nesnesi olusturdum.
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):                    # Dugumlerin icerisinden aranan dugume ulasabilmek icin get_vertex() fonksiyonunu yazdim ve parametre olarak dugumun ismini aldim.               
        if n in self.vert_dict:                 # Eklenen tum vertexlerin icinde aranan vertex var ise aranan vertexi dondurecek kosulu yazdim.
            return self.vert_dict[n]
        else:                                   # Vertex bulunamamissa fonksiyon ciktisi olarak None dondurdum
            return None

    def add_edge(self, frm, to):                # Vertexler (Dugumler) arasindaki komsuluklari ve yol maliyetini kaydetmek icin add_edge() fonksiyonunu olusturdum.
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to])
        self.vert_dict[to].add_neighbor(self.vert_dict[frm])

def DegreeHeuristic(g, cities, q):              # En cok komsusu olana ilk deger atamasi yapabilmek icin kullanacagim Degree Heuristic icin fonksiyon olusturdum.
    queue = []                                  # Bos bir liste olusturdum.
    for i in range(len(cities)):                # Butun sehirleri kontrol edecek ve kuyruga ekleyecek donguyu yazdim.
        q.put((int(g.get_vertex(cities[i]).get_NeighborCount()), str(cities[i])))   # Her bir dugumu komsu sayisina gore siralanacak sekilde priority queue'ye aktardim.
    
    while not q.empty():                        # Priority queue kucukten buyuge siraladigi icin bu sirayi tersine dondurecek donguyu yazdim.
        current = q.get()
        queue += [current[1]]
    queue.reverse()
    print(queue)
    return queue                                # Fonksiyon ciktisi olarak Liste dondurdum.

def MapColoring(g, cities,domains):             # Haritayi boyamak icin MapColoring fonksiyonunu olusturdum.
    List = DegreeHeuristic(g,cities,q = pq())   # Oncelik listesini Degree Heuristic fonksiyonu ile olusturdu.
    while len(List)>0:                          # Listedeki her dugum isleme alinana kadar donguye devam edebilmek icin bir while dongusu olusturdum.
        domain_current = []                     # Gecici olacak domain listesi icin bir liste olusturdum.
        for i in range(len(domains)):           # Her bir domain icin gecici domain listesine atama yaptim.
            domain_current.append(domains[i])
        current = List[0]                       # Gecici degisken olusturdum ve domain listesinin ilk degerini bu degiskene atadim.
        for i in range(len(domains)):           # Her bir domain icin islem yapacak donguyu olusturdum.
            control = 0                         # Dugumun alamayacagi renkleri domain listesinden silebilmek icin bir kontrol degiskeni atadim.
            for j in range(len(g.get_vertex(current).get_neighbors())): # Gecici dugumun tum komsularini kontrol ettim ve renk almis olanlarin aldiklari rengi gecici dugumun domain listesinden kaldirdim.
                if domains[i] == g.get_vertex(g.get_vertex(current).get_neighbors()[j]).color:
                    control = 1
            if control != 0 and domains[i] in domain_current:
                domain_current.remove(domains[i])
        g.get_vertex(current).posibility = domain_current   # Gecici dugumun domain listesini atadim.
        List.remove(current)                    # Renlendirilmis dugumu Listeden kaldirdim.

        if len(g.get_vertex(current).posibility) > 0:       # Eger gecici dugumun alabilecegi renkler var ise yani domaini bos degil ise yapilacak islemleri yazdim.
            g.get_vertex(current).color = g.get_vertex(current).posibility[0]   # Gecici dugumun rengine domaini icindeki ilk renk degiskenini atadim.
            for i in range(len(g.get_vertex(current).get_neighbors())): # Gecici dugumun komsularinin domainlerini duzenlemek icin bir dongu olusturdum.
                iter_domain = []                            # Domainleri atayabilmek icin bos bir liste olusturdum.
                for j in range(len(domains)):               # Tanimlanmis tum domainler icin islem yapacak donguyu olusturdum.
                    if domains[j] != g.get_vertex(current).color: # Gecici dugume verilen renk haricindeki domainleri yeni listeye ekledim.
                        iter_domain.append(domains[j])
                g.get_vertex(g.get_vertex(current).get_neighbors()[i]).posibility = iter_domain # Gecici dugumun komsularinin domainlerini atadim.
            domain_current.remove(g.get_vertex(current).color)  # Gecici dugumun domainlerinden aldigi rengi sildim.
            g.get_vertex(current).posibility = domain_current

if __name__ == '__main__':          # Asil islemlerin yapilacagi ana fonksiyonu yani main fonksiyonu yazdim.

    g = Graph()                     # Sehirlerin komsuluklarini olusturabilmek icin bir graph olusturdum.
                                    # Bir liste olusturdum ve bu listeye sehirlerin isimlerini girdim.
    Cities = ['İzmir','Manisa','Aydın','Muğla','Kütahya','Uşak','Denizli','Afyonkarahisar'] 
                                    # Bir liste olusturdum ve bu listeye domainleri girdim.
    domain_list = ['Yeşil','Kırmızı','Beyaz']

    for i in range(len(Cities)):    # Her bir sehiri graph'a ekleyecek for dongusunu olusturdum.
        g.add_vertex(Cities[i]).posibility = domain_list    # Her bir sehiri domainleri ile birlikte graph'a ekledim.
                                            # Sehirlerin Komsuluklarini ekledim.
    g.add_edge('İzmir','Manisa')            # Izmir Manisa Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('İzmir','Aydın')             # Izmir Aydin Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Manisa','Kütahya')          # Manisa Kutahya Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Manisa','Uşak')             # Manisa Usak Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Manisa','Denizli')          # Manisa Denizli Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Aydın','Muğla')             # Aydin Mugla Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Aydın','Denizli')           # Aydin Denizli Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Muğla','Denizli')           # Mugla Denizli Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Kütahya','Uşak')            # Kutahya Usak Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Kütahya','Afyonkarahisar')  # Kutahya Afyonkarahisar Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Uşak','Afyonkarahisar')     # Usak Afyonkarahisar Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Uşak','Denizli')            # Usak Denizli Sehirlerinin Komsuluklarini ekledim.
    g.add_edge('Denizli','Afyonkarahisar')  # Denizli Afyonkarahisar Sehirlerinin Komsuluklarini ekledim.


    MapColoring(g,Cities,domain_list)       # MapColoring fonksiyonunu calistirdim.

    print('Şehirlerle ilgili tüm bilgiler : ',end='\n\n')   # Sehirlerle ilgili bilgileri ekrana yazdirdim.
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ("( %s , %s)"  % (vid, wid))
    print('')
    for v in g:
        print ('%s Şehrinin rengi : ' %( v.get_id() ),end='')   # Sehirlerin aldiklari renkleri yazdirdim.
        print(g.get_vertex(v.get_id()).color)