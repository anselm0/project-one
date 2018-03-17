import matplotlib.pyplot as plt
import pandas as pd
import datetime

target_path = "Merged/"

target_csv_list = [target_path + "@WSJ_all.csv"]
                   
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
    df['Date'] = pd.to_datetime(df['Date'], format= '%Y-%m-%d')
    x = df['Date'].values
    vader = df['Vader'].values
    textblob = df['TextBlob'].values
    
    #SPX
    y = df['SPX Price'].values
    volume = (df['SPX Volume'].values)/10000000
    
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(2600, 2800)
    ax.set_xlim([datetime.date(2018,2,10), datetime.date(2018,3,18)])
    
    ax.scatter(x, y, s=volume, c=vader, cmap='RdYlGn', alpha=0.5)
    ax.plot(x,y)
    
    ax.grid(True)
    fig.tight_layout()
    
    
    
    ax.set_title('WS_SPX')
    
    #DJI
    y = df['DJI Price'].values
    volume_dji = (df['DJI Volume'].values)/1000000
    
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(24000, 26000)
    ax.set_xlim([datetime.date(2018,2,10), datetime.date(2018,3,18)])

    
    ax.scatter(x, y, s=volume_dji, c=vader, cmap='RdYlGn', alpha=0.5)
    ax.plot(x,y)
    
    ax.grid(True)
    fig.tight_layout()
    
    
    
    ax.set_title('WSJ_DJI')
    
    #NDX
    y = df['NDX Price'].values
    volume_ndx = (df['NDX Volume'].values)/10000000
    
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(6400, 7200)
    ax.set_xlim([datetime.date(2018,2,10), datetime.date(2018,3,18)])
    
    ax.scatter(x, y, s=volume_ndx, c=vader, cmap='RdYlGn', alpha=0.5)
    ax.plot(x,y)

    
    ax.grid(True)
    fig.tight_layout()
    
    
    
    ax.set_title('WSJ_NDX')
    
    #add legends and fix x labels
    #make graph larger
    #border around bubbles
    #add interactivity with mouse overs
    #save the figures as jpgs to a folder
    
    
