import matplotlib.pyplot as plt
import pandas as pd

target_path = "Merged/"

target_csv_list = [target_path +"@FT_all.csv"]

'''
                   target_path + "@FT_all.csv", 
                   target_path + "@nyTimes_all.csv", 
                   target_path + "@barronsonline_all.csv", 
                   target_path + "@IBDinvestors_all.csv",
                   target_path + "@CNN_all.csv", 
                   target_path + "@wired_all.csv", 
                   target_path + "@business_all.csv", 
                   target_path + "@USAToday_all.csv", 
                   target_path + "@FoxBusiness_all.csv"]
                                                        
'''

for csv_item in target_csv_list:
    
    df = pd.read_csv(csv_item, index_col = False)
    x = df.index
    vader = df['Vader'].values
    textblob = df['TextBlob'].values
    
    #SPX
    y = df['SPX Price'].values
    volume = (df['SPX Volume'].values)/7000000
    
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(2600, 2800)
    
   
    sc=ax.scatter(x, y, s=volume, c=vader, cmap='RdYlGn',edgecolor = 'black', alpha=0.8)
    
    
    ax.grid(True)
    
    fig.tight_layout()
    
    #Won't add labels still working on it
    #ax.set_xlabel = ('Days')
    #ax.set_ylabel=('Price')
    ax.set_title('Financial Times Sentiment (Vader) with SPX Price and Volume')
    ax.title.set_position([.5,1.05])
    cbar=plt.colorbar(sc)
    cbar.set_label('Polarity',rotation = 270,labelpad=10)
    

    #plt.savefig('FTvader_SPX_spv.png',bbox_inches="tight")             
    plt.show()
    #add legends and fix x labels
    #make graph larger
    #border around bubbles
    #add interactivity with mouse overs
    #save the figures as jpgs to a folder
    
    
