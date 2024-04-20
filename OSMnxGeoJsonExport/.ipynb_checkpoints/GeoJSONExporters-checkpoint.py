class GeoJSONPointExporter:

    def __init__(self, latitude, longitude, radius):

        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.networkType = "walk"
        self.nodeColor = "#2ac1db"
        self.edgeColor = "#e38d3d"
        self.backgroundColor = "#ffffff"

    def getGraph(self):
        graph = ox.graph.graph_from_point((self.latitude, self.longitude), dist = self.radius, dist_type = 'bbox', network_type = self.networkType, simplify = True)
        return graph

    def drawGraph(self, exportPath):
        graph = self.getGraph()
        if(exportPath != ""):
            fig, ax = ox.plot_graph(graph, node_color = self.nodeColor, edge_color = self.edgeColor, bgcolor = self.backgroundColor)
            fig.savefig(exportPath, bbox_inches = "tight")
        else:
            fig, ax = ox.plot_graph(graph)

    def cleanDataFrame(self, dataFrame):
        #Why is traversing pandas data structures so hard?
        keys = dataFrame.keys()
        element = -1
        for i in range(0,len(keys)):
            key = keys[i]
            subKeys = dataFrame[key].keys()
            for j in range(0,len(subKeys)):
                subKey = subKeys[j]
                if(type(dataFrame[key][subKey]) is list):
                    dataFrame.loc[subKey, key] = str(dataFrame.loc[subKey, key])

        return dataFrame

    def exportToGeoJSON(self, path):
        #First we convert to the geodataframe used in pandas
        graph = self.getGraph()
        dataFrameNodes, dataFrameEdges = ox.graph_to_gdfs(graph)
        #I think it is important to add the distance, and it has to be a projected distance
        #ox.distance_add_edge_lengths(graph, precision = None, ed)
        #Clean the nodes, we cannot have lists
        cleanedDataFrame = self.cleanDataFrame(dataFrameEdges)
        cleanedDataFrame.to_file(path, driver = 'GeoJSON')

        print("Exported the json")
        
        return cleanedDataFrame

class GeoJSONPlaceExporter:

    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country
        self.networkType = "walk"
        self.nodeColor = "#2ac1db"
        self.edgeColor = "#e38d3d"
        self.backgroundColor = "#ffffff"

    def getGraph(self):
        place = {"city": self.city, "state": self.state, "country":self.country}
        graph = ox.graph.graph_from_place(place, network_type = self.networkType, truncate_by_edge = True, simplify = True)
        return graph


    def drawGraph(self, exportPath):
        graph = self.getGraph()
        if(exportPath != ""):
            fig, ax = ox.plot_graph(graph, node_color = self.nodeColor, edge_color = self.edgeColor, bgcolor = self.backgroundColor, node_size = 0.1, edge_linewidth = 0.1)
            fig.savefig(exportPath, bbox_inches = "tight")
        else:
            fig, ax = ox.plot_graph(graph)

    def cleanDataFrame(self, dataFrame):
        #Why is traversing pandas data structures so hard?
        keys = dataFrame.keys()
        element = -1
        for i in range(0,len(keys)):
            key = keys[i]
            subKeys = dataFrame[key].keys()
            for j in range(0,len(subKeys)):
                subKey = subKeys[j]
                if(type(dataFrame[key][subKey]) is list):
                    dataFrame.loc[subKey, key] = str(dataFrame.loc[subKey, key])

        return dataFrame

    def exportToGeoJSON(self, path):
        #First we convert to the geodataframe used in pandas
        graph = self.getGraph()
        dataFrameNodes, dataFrameEdges = ox.graph_to_gdfs(graph)
        #I think it is important to add the distance, and it has to be a projected distance
        #ox.distance_add_edge_lengths(graph, precision = None, ed)
        #Clean the nodes, we cannot have lists
        cleanedDataFrame = self.cleanDataFrame(dataFrameEdges)
        cleanedDataFrame.to_file(path, driver = 'GeoJSON')

        print("Exported the json")
        
        return cleanedDataFrame
        



        


