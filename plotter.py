import matplotlib.pyplot as plt
import pandas as pd
import datetime

target_path = "Merged/"

target_csv_list = [target_path + "@WSJ_all.csv",
                   target_path + "@FT_all.csv", 
                   target_path + "@nyTimes_all.csv", 
                   target_path + "@barronsonline_all.csv", 
                   target_path + "@IBDinvestors_all.csv",
                   target_path + "@CNN_all.csv", 
                   target_path + "@wired_all.csv", 
                   target_path + "@business_all.csv", 
                   target_path + "@USAToday_all.csv", 
                   target_path + "@FoxBusiness_all.csv"]
                                                        
for csv_item in target_csv_list:
    
    font = {'family': 'sans-serif',
            'color':  'darkred',
            'weight': 'bold',
            'size': 18,
            }
    
    df = pd.read_csv(csv_item, index_col = False)
    df['Date'] = pd.to_datetime(df['Date'], format= '%Y-%m-%d')
    x = df['Date'].values
    vader = df['Vader'].values
    textblob = df['TextBlob'].values
    plot_path = "Plots/"

    
    #SPX
    y = df['SPX Price'].values
    volume = (df['SPX Volume'].values)/10000000
    
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(2600, 2800)
    ax.set_xlim([datetime.date(2018,2,10), datetime.date(2018,3,18)])
    
    sc = ax.scatter(x, y, s=volume, c=textblob, cmap='RdYlGn', alpha=0.5, edgecolor = 'black')
    ax.plot(x,y)
    
    ax.grid(True, alpha=.5)
    fig.tight_layout()
    
    title = '{} Sentiment vs SP500'.format(csv_item[7:-8])
    ax.set_title(str(title), fontdict=font)
    ax.set_ylabel('Price')
    plt.xticks(rotation=45)
    fig.colorbar(sc, spacing='proportional').set_label('Sentiment Polarity',rotation = 270,labelpad=10)
    fig.set_size_inches(9, 6)
    fig.savefig(plot_path + csv_item[7:-8] + '_SPX_plot_textblob.png',bbox_inches="tight", dpi=72)  
    
    #DJI
    y = df['DJI Price'].values
    volume_dji = (df['DJI Volume'].values)/1000000
    
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(24000, 26000)
    ax.set_xlim([datetime.date(2018,2,10), datetime.date(2018,3,18)])

    
    sc = ax.scatter(x, y, s=volume_dji, c=textblob, cmap='RdYlGn', alpha=0.5, edgecolor = 'black')
    ax.plot(x,y)
    
    ax.grid(True, alpha=.5)
    fig.tight_layout()
    
    title = '{} Sentiment vs Dow Jones'.format(csv_item[7:-8])
    ax.set_title(str(title), fontdict=font)
    ax.set_ylabel('Price')
    plt.xticks(rotation=45)
    fig.colorbar(sc, spacing='proportional').set_label('Sentiment Polarity',rotation = 270,labelpad=10)
    fig.set_size_inches(9, 6)
    fig.savefig(plot_path + csv_item[7:-8] + '_DJI_plot_textblob.png',bbox_inches="tight", dpi=72)  

    
    #NDX
    y = df['NDX Price'].values
    volume_ndx = (df['NDX Volume'].values)/10000000
    
    
    fig, ax = plt.subplots()
    
    ax.set_ylim(6400, 7200)
    ax.set_xlim([datetime.date(2018,2,10), datetime.date(2018,3,18)])
    
    sc = ax.scatter(x, y, s=volume_ndx, c=textblob, cmap='RdYlGn', alpha=0.5, edgecolor = 'black')
    ax.plot(x,y)

    
    ax.grid(True, alpha=.5)
    fig.tight_layout()
    
    
    title = '{} Sentiment vs NASDAQ'.format(csv_item[7:-8])
    ax.set_title(str(title), fontdict=font)
    ax.set_ylabel('Price')
    plt.xticks(rotation=45)
    fig.colorbar(sc, spacing='proportional').set_label('Sentiment Polarity',rotation = 270,labelpad=10)
    fig.set_size_inches(9, 6)
    fig.savefig(plot_path + csv_item[7:-8] + '_NDX_plot_textblob.png',bbox_inches="tight", dpi=72)  

    #add legends and fix x labels
    #make graph larger
    #add interactivity with mouse overs    
    
