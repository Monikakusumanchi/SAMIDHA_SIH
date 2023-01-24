# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:32:24 2022

@author: user
"""

import numpy as np
import pickle
import streamlit as st
#from sklearn.preprocessing import StandardScaler

loaded_model=pickle.load(open('E:/samidha_SIH/dredger_1/dredger_calculator.sav', 'rb'))
def fuel_predict(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return prediction
#	fuel_consumed(lt/hr)	total_power(kW)		Required Pump Power	Required Cutter Power
def power_predict(input_data1):
    
    input_data_as_numpy_array1 = np.asarray(input_data1)

# reshape the array as we are predicting for one instance
    input_data_reshaped1 = input_data_as_numpy_array1.reshape(1,-1)

# standardize the input data
    
    prediction1 = loaded_model.predict(input_data_reshaped1)
    print(prediction1)
    return prediction1
def main():
    
    st.title('VESSEL OUTPUT CALCULATOR')
    st.write('Dredger Calculator')
    st.write("0. Silt")
    st.write("1. Fine sand")
    st.write("2. Coarse sand")
    st.write("3. Gravel")
    type_of_land =st.text_input("type of land:")
    
   					
    #type_of_land =st.text_input('enter type of land')
    st.write("0. Cutter suction dredger with two spuds")
    st.write("1. Cuttre suction dredger with spudcarrier")
    st.write("2. Plain suction dredger")
    type_of_dredger=st.text_input("enter type of dredger") 
    #length_of_channel=st.text_input("enter the length of channel to be dredged")
    
    #pipeline_material=st.text_input("enter the type of pipeline material")
    volume =st.text_input('enter volume of mixture to be dredged')
    st.write("0. Steel")
    st.write("1. HDPE")
    type_of_pipe=st.text_input("enter the type of dredger pipe")
    
    total_working_days=st.number_input('enter total working days per week')
    working_hours_per_day=st.number_input('enter total working hours per day')
    
    total_working_hours =total_working_days*working_hours_per_day
    
    #fuel_consumed=st.text_input("enter the fuel consumed")
   
    if st.button("fuel predection in l/h"):
        pred =fuel_predict([type_of_land,type_of_dredger,volume,total_working_hours])
        st.write("fuel consumed lt/hr and power consumed kw",pred[0])
        #st.write("total_power_consumed kw",pred[1])
        #st.write("Required Pump Power", pred(1)*0.7)
        #st.write("Required Cutter Power", pred(1)*0.3)
    #if st.button("total power used"):
     #   pred1 =fuel_predict([type_of_land,type_of_dredger,fuel_consumed,volume,total_working_hours])
      #  st.write(pred1)
  
      
        st.markdown(
    """
    ### 💾 The consolitated report :
    **Column Name**|**Description**
    -----|-----
    |fuel consumed lt/hr %d|198|
    |total_power_consumed|849|
    |Required Pump Power|138|
    |Required Cutter Power|245|
    |Effective working hours|657|
    |average_fuel_consumption|24.75 |
    """
        )
    
if __name__=='__main__':
    main()
   