import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import locale

# A hello world matplotlib plot
plt.plot(range(20))
plt.show()

fig = plt.figure(figsize=[4,4])
ax1 = fig.add_axes([0,0,1,1])
ax1.plot(range(20))
fig.show()

# another example
import numpy as np
fig = plt.figure(figsize=[12,12])
ax1=fig.add_axes([0,0,1,1])
# set the number of points to be displayed
numpoints=100
# we want to color the points randomly
rgba_colors = np.zeros((numpoints,4))
# fill in first 3 columns with random percentage for red, green, blue
for ii in range(0,3):
    rgba_colors[:,ii] = np.random.uniform(low=0.1,high=0.9,size=numpoints)
# the fourth column sets the transparency
rgba_colors[:,3] = np.random.uniform(low=0.1,high=0.9,size=numpoints)

ax1.scatter(np.random.random_integers(low=0,high=100,size=numpoints),
            np.random.random_integers(low=0,high=100,size=numpoints),
            s=np.random.random_integers(low=100,high=500,size=numpoints),
            color=rgba_colors)
fig.show()


# plot with pandas
Data = pd.read_csv("Dataset.csv")
Data['ID'].head()

Data.Benefit_Amt.hist(figsize=[8,6])
Data[['Benefit_Amt','Citizenship']].hist(by='Citizenship',figsize=[8,6])

mark = Data['Overpayment_Amount']==' '
Data['Overpayment_amt']=Data['Overpayment_Amount']
Data.ix[mark,'Overpayment_amt']=0
Data['Overpayment_amt']=Data['Overpayment_amt'].apply(lambda x:float(x))

Data.ix[Data['Overpayment_amt']>0,['Overpayment_amt','Citizenship']].hist(by='Citizenship',figsize=[16,6])
# scatter plot
Data.plot(kind='scatter',x='Rent_Amount',y='Monthly_Benefit',figsize=[10,8],s=100)
Data[Data['Overpayment_amt']>0].plot(kind='scatter',x='Rent_Amount',y='Monthly_Benefit',figsize=[10,8],s=100)

# Advanced
# Define a few formatters and colors
from matplotlib.ticker import FuncFormatter
### define a few Deloitte-branded colors
## core secondary colors
deloitte_light_blue = '#1462FF'
deloitte_medium_grey = '#7F7F7F'

## core primary colors
deloitte_very_light_blue = '#00A1DE'
deloitte_dark_blue = '#002776'

## supporting primary colors
deloitte_salad_green = '#92D400'
deloitte_charcoal_grey = '#65727E'

### define a few utility formatters

def to_percent(y,position):
    s = str(100*y)
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

def to_count(y,position):
    try:
        locale.setlocale(locale.LC_ALL,'en_US')
    except:
        locale.setlocale(locale.LC_ALL,'us')
    s = str(locale.format("%d",y,grouping=True))
    
    if matplotlib.rcParams['text.usetex'] == True:
        return s
    else:
        return s

## an important function to format plot area
def format_axis(ax):
    ## remove grid lines
    ax.grid(b=False)
    ## remove background
    ax.set_axis_bgcolor('white')
    

# Then define the plotting function itself. The function uses the final level access
# to plot customization provided by matplotlib
def make_prevalence_sample_size_plot (dataframe, bars_colname, legend_colname,
                                      subset_value=1, kind='bar',figsize=[8,8],
                                      title='',
                                      y_primary_title='',
                                      y_secondary_title='',
                                      sample_size_label='',
                                      legend_position='upper left',
                                      verbatim=False):

    work = dataframe[[legend_colname,bars_colname]].copy()
    dummy_colname = 'dummy'
    work.loc[:,dummy_colname] = pd.Series(0,index=work.index)

## group by the variables, calculate group totals
    te = work.groupby([legend_colname,bars_colname])[dummy_colname].count().reset_index()
    df = te.pivot(index=bars_colname,columns=legend_colname,values=dummy_colname)

## calculate percentages
    dfp = df.transpose()/df.transpose().sum()
    dfp1 = dtp.transpose()
    dtp1.head()

## extract percentages to plot
    plot_values = dfp1[subset_value]
    plot_values[plot_values.isnull()] = 0


## extract sample sizes to plot
## this lets sample size be the subset_value group count
## sample_size = df[subset_value]
## this lets sample size be the total group count (subset_value and not)
    sample_size = df.transpose().sum()
    sample_size[sample_size.isnull()] = 0

    if verbatim:
        try:
            locale.setlocale(locale.LC_ALL,'en_US')
        except:
            # for windows
            locale.setlocale(locale.LC_ALL,'us')
            forprint = sample_size.apply(lambda x: str(locale.format("%d",x,grouping=True)))
            print forprint

# display bar plot
    ax1 = plot_values.plot(kind=kind,figsize=figsize,title=title,color=deloitte_very_light_blue)
    format_axis(ax1)

    if y_primary_title != '':
        ax1.set_ylabel(y_primary_title)

## display percentage values on top of bars
    count = 0
    for rect in ax1.patches:
        height = rect.get_height()
        lab = str(round(plot_values.tolist()[count]*100,1)) + '%'
        ax1.text(rect.get_x()+rect.get_width()/2.,rect.get_y()+height,lab,ha='center',va='bottom')
        count=count+1
    
# format y axis to show percent
    formatter = FuncFormatter(to_percent)
    ax1.yaxis.set_major_formatter(formatter)

# plot sample size as a line plot on secondary axis
    ax2 = ax1.twinx()
    format_axis(ax2)

# format y axis to show sample size
    formatter = FuncFormatter(to_count)
    ax2.yaxis.set_major_formatter(formatter)

    ax2.plot(ax1.get_xticks(),sample_size.tolist(),linewidth=3, dashes=[5,5],color=deloitte_salad_green,
         label=sample_size_label)

    if y_secondary_title != '':
        ax2.set_ylabel(y_secondary_title)

    if sample_size_label != '':
        legend = ax2.legend(loc=legend_position)
        frame = legend.get_frame()
        frame.set_facecolor('white')
    
# With the plotting function defined, we can make a few useful plots
data['Overpayment_indicator'] = (data['Overpayment_amt']>0).apply(lambda x:int(x))

make_prevalence_sample_size_plot(data,'Citizenship','Overpayment_indicator',
                                 subset_value=1,kind='bar',figsize=[8,8],
                                 title='Percent overpayment by citizenship verification status',
                                 y_primary_title = 'Percent overpayments',
                                 y_secondary_title = 'Number of payment-months',
                                 sample_size_label = '# payments',
                                 legend_position='upper left',
                                 verbatim=True)
                                 



















    
    














