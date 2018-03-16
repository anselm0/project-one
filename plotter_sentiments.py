import matplotlib.pyplot as plt
import pandas as pd

target_path = "Merged/"

target_csv_list = [target_path +"@FoxBusiness_all.csv"]

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
    y1 = vader
    y2=textblob
    #volume = (df['SPX Volume'].values)/7000000
    
    
  
    #ax.set_ylim(2600, 2800)
    
    plt.title('Average Sentiment for past 30 days for @FoxBusiness')
    vader_plt ,= plt.plot(x,y1,marker='o',alpha=.5,label='Vader Polarity')
    textblob_plt ,= plt.plot(x,y2,marker='o',alpha=.5,label='TextBlob Polarity')
    plt.legend(handles=[vader_plt,textblob_plt])
    plt.xlabel('Days')
    plt.ylabel('Polarity')
    plt.savefig('foxbusiness.png',bbox_inches="tight")

    plt.show()
    #ax.scatter(x, y, s=volume, c=textblob, cmap='RdYlGn', alpha=0.5)
    
    #ax.grid(True)
    #fig.tight_layout()
    
    #plt.title('WSJ Average Sentiment for past 30 days')
    
    #add legends and fix x labels
    #make graph larger
    #border around bubbles
    #add interactivity with mouse overs
    #save the figures as jpgs to a folder
    
    
