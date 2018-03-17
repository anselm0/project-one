import matplotlib.pyplot as plt
import pandas as pd


target_path = "Merged/"

target_csv_list = [target_path +"@wired_all.csv"]

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
    #x=df['NDX Price'].values
    x = df.index
    #vader = df['Vader'].values
    #textblob = df['TextBlob'].values
    
    #SPX, DJI, NDX
    y=(df['DJI Price'].values)
    #y=(df['NDX Price'].values)
    #y = df['SPX Price'].values
    volume = (df['DJI Volume'].values)/1000000
    
   
    fig, ax = plt.subplots()

    #ax.set_ylim(2625, 2800)
    ax.set_ylim(24450, 25600)
    
    #sc=ax.scatter(x, y, s=250, alpha=0.8, edgecolor='black')

    sc=ax.scatter(x, y,s=volume, c=volume, cmap='cool', alpha=0.8, edgecolor='black')
    ax.grid(True)
    plt.colorbar(sc)
    plt.tight_layout()

    plt.xlabel('Days')
    plt.ylabel('Price')
    ax.set_title('DJI Price and Volume over 30 Days')
    plt.savefig('DJI_pricevol.png',bbox_inches="tight")

    plt.show()
      
    #add legends and fix x labels
    #make graph larger
    #border around bubbles
    #add interactivity with mouse overs
    #save the figures as jpgs to a folder
    
    
