import pandas as pd
import matplotlib.pyplot as plt

def Project():
   try:
       CovData = pd.read_csv('covid20.csv')
       #print(CovData.head())
     #  print(CovData.columns)
       print(f' The data is  {CovData.isnull().sum()}')
      # CovData.dropna(axis =0, inplace= True)
        
       #print(f' The data is  {CovData.isnull().sum()}')
       print(CovData.head())
       CovData.fillna(0, inplace = True)
       print(CovData.head())

    # Time 
       CovData['Last Update'] = pd.to_datetime(CovData['Last Update'])
       CovData['hour'] =  CovData['Last Update'].dt.hour #Extracting Hours
     #Plotting
     #  plt.plot(CovData['Deaths'], CovData['Confirmed'])  
       try:
           CovData['Province/State'] = CovData['Province/State'].astype(str)
           provDat = CovData.groupby('Province/State')['Deaths'].sum()
           plt.bar(provDat.index, provDat.values)
           plt.xlabel('Province/State')
           plt.ylabel('Deaths')
           plt.show()
        #plt.plot(CovData['Province/State'], CovData['Deaths'], kind = 'Hist')

       except Exception as e:
           print(f'The problem is at the {e}')
       
       plt.xlabel('Hour')
       plt.ylabel('Victims')
       #Calculations
       deathRate = CovData['Confirmed'].agg('sum') / CovData['Deaths'].agg('sum')
       print(f'the deathRate is {deathRate}')
       
    
        
    
       



   except Exception as e:
        print(f"Hey {e}")



Project()