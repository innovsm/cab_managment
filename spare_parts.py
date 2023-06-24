import  mysql.connector
import streamlit as st


def get_driver():
    connector = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_shubhanshumishra",
    password="!ata%t$Fk39QF6!",
    database="freedb_CabManagment"
    )
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM driver")
    final_list = []
    for i in cursor:
        final_list.append(i)
    return final_list

def update_driver(driver_id,new_driver_id, driver_name,driver_email, driver_phone):
        connector = mysql.connector.connect(
                            host="sql.freedb.tech",
                            user="freedb_shubhanshumishra",
                            password="!ata%t$Fk39QF6!",
                            database="freedb_CabManagment"
                            )
        mycursor = connector.cursor()
        sql = "UPDATE driver SET driver_id = %s, driver_name = %s, email = %s, phone_number = %s WHERE driver_id = %s"
        val = (int(new_driver_id), driver_name, driver_email, driver_phone, int(driver_id))
        mycursor.execute(sql, val)
        connector.commit()
        return "succes"

def get_driver_specific(driver_id):
    connector = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_shubhanshumishra",
    password="!ata%t$Fk39QF6!",
    database="freedb_CabManagment"
    )
    cursor = connector.cursor()
    query = "SELECT * FROM driver WHERE driver_id = %s"
    val = (driver_id,)
    cursor.execute(query, val)

    final_list = []
    for i in cursor:
        final_list.append(i)
    return final_list
# ==========================================================================================
def driver_app():
    st.title = "Driver Management"
    st.subheader("This is the driver management page")
    with st.expander("Modify Driver Database", expanded = False):
        operation_select = st.selectbox("Select Operation", ["","Add Driver", "Remove Driver", "Update Driver"])
        if(operation_select == "Add Driver"):
            driver_id = st.text_input("Enter Driver ID",max_chars=10, key="driver_id", help="Enter Driver ID")
            driver_name = st.text_input("Enter Driver Name",max_chars=50, key="driver_name", help="Enter Driver Name")
            driver_email = st.text_input("Enter Driver Email",max_chars=50, key="driver_email", help="Enter Driver Email")
            driver_phone = st.text_input("Enter Driver Phone",max_chars=10, key="driver_phone", help="Enter Driver Phone")
            submit_button = st.button("Add Driver")
            # checking each value

            if(driver_id and driver_name and driver_email and driver_phone):
                # clearing the input fields
                
                #print(driver_id, driver_name, driver_email, driver_phone)
                if(submit_button == True):
                    # adding driver to database
                 
                    try:

                    
                        connector = mysql.connector.connect(
                            host="sql.freedb.tech",
                            user="freedb_shubhanshumishra",
                            password="!ata%t$Fk39QF6!",
                            database="freedb_CabManagment"
                            )
                        mycursor = connector.cursor()
                        sql = "INSERT INTO driver (driver_id, driver_name, email, phone_number) VALUES (%s, %s, %s, %s)"
                        val = (int(driver_id), driver_name, driver_email, driver_phone)
                        mycursor.execute(sql, val)
                        connector.commit()
                        st.success("Driver Added Successfully")
                    except:
                        st.error("Driver ID already exists")
                    finally:
                        mycursor.close()
                        connector.close()
        elif(operation_select == "Remove Driver"):
            # calling driver list
            try:

          
                final_list = get_driver()
                driver_id = st.selectbox("Select Driver ID",[""]+[[i[0],i[1]] for i in final_list])
                submit_button = st.button("Remove")
                # deleing the selected user
                if(submit_button == True):
                    connector = mysql.connector.connect(
                        host="sql.freedb.tech",
                        user="freedb_shubhanshumishra",
                        password="!ata%t$Fk39QF6!",
                        database="freedb_CabManagment"
                        )
                    mycursor = connector.cursor()
                    sql = "DELETE FROM driver WHERE driver_id = %s"
                    val = (driver_id[0],)
                    mycursor.execute(sql, val)
                    connector.commit()
                    st.success("Driver Removed Successfully")
            except:
                st.error("Either Driver list is empty or driver has been assigned a cab")
        if(operation_select == "Update Driver"):
            st.subheader("Update Driver")
            
            final_list = get_driver()
            driver_id = st.selectbox("Select Driver ID", [""]+[[i[0],i[1]] for i in final_list])
            submit_button = st.button("Search")
            if(len(driver_id) > 1):
                try:
                    data = get_driver_specific(driver_id[0])
                    driver_id_new = st.text_input("Enter Driver ID",value = data[0][0],max_chars=10, key="driver_id_new", help="Enter Driver ID")
                    driver_name_new = st.text_input("Enter Driver Name",value = data[0][1],max_chars=50, key="driver_name_new", help="Enter Driver Name")
                    driver_email_new = st.text_input("Enter Driver Email",value = data[0][2],max_chars=50, key="driver_email_new", help="Enter Driver Email")
                    driver_phone_new = st.text_input("Enter Driver Phone",value = data[0][3],max_chars=10, key="driver_phone", help="Enter Driver Phone")
                    submit_button_1 = st.button("Update")
                    if(submit_button_1):

                        print("1")
                        update_driver(driver_id[0],driver_id_new, driver_name_new,driver_email_new, driver_phone_new)
                        print("2")
                        st.success("Driver Updated Successfully")
                except Exception as e:
                    print("An error occurred:", e)

         
     

# ======================================[Cab Area] ====================================================

# ==========================================================================================
def update_cab(new_cab_id, cab_model,cab_color,cab_id):
        connector = mysql.connector.connect(
                            host="sql.freedb.tech",
                            user="freedb_shubhanshumishra",
                            password="!ata%t$Fk39QF6!",
                            database="freedb_CabManagment"
                            )
        mycursor = connector.cursor()
        sql = "UPDATE cabs SET cab_registration_number = %s, model = %s, color = %s WHERE cab_registration_number = %s"
        val = (new_cab_id, cab_model , cab_color,cab_id)
        mycursor.execute(sql, val)
        connector.commit()
        return "succes"

def get_cabs():
    connector = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_shubhanshumishra",
    password="!ata%t$Fk39QF6!",
    database="freedb_CabManagment"
    )
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM cabs")
    final_list = []
    for i in cursor:
        final_list.append(i)
    return final_list

def get_cab_specific(cab_id):
    connector = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_shubhanshumishra",
    password="!ata%t$Fk39QF6!",
    database="freedb_CabManagment"
    )
    cursor = connector.cursor()
    query = "SELECT * FROM cabs WHERE cab_registration_number = %s"
    val = (cab_id,)
    cursor.execute(query, val)

    final_list = []
    for i in cursor:
        final_list.append(i)
    return final_list
# ==========================================================================================


def cab_app():
    st.title = "Cab Management"
    st.subheader("This is the Cab management page")
    with st.expander("Modify Cab Database", expanded = False):
        operation_select = st.selectbox("Select Operation", ["","Add Cab", "Remove Cab", "Update Cab"])
        if(operation_select == "Add Cab"):
            cab_id = st.text_input("Enter Cab Regestration Number",max_chars=20, key="driver_id", help="Enter Driver ID")
            cab_model = st.text_input("Enter Cab Model Name",max_chars=50, key="driver_name", help="Enter Driver Name")
            cab_color = st.text_input("Enter Cab Color",max_chars=15, key="driver_email", help="Enter Driver Email")

            submit_button = st.button("Add Cab")
            # checking each value

            if(cab_id and cab_model and cab_color):
                # clearing the input fields
                
                #print(cab_id, cab_model, cab_color)
                if(submit_button == True):
                    # adding driver to database
                 
                    try:

                    
                        connector = mysql.connector.connect(
                            host="sql.freedb.tech",
                            user="freedb_shubhanshumishra",
                            password="!ata%t$Fk39QF6!",
                            database="freedb_CabManagment"
                            )
                        mycursor = connector.cursor()
                        sql = "INSERT INTO cabs (cab_registration_number, model, color) VALUES (%s, %s, %s)"
                        val = (cab_id, cab_model, cab_color)
                        mycursor.execute(sql, val)
                        connector.commit()
                        st.success("Cab Added Successfully")
                    except:
                        st.error("Either Cab ID already exists or Cab has been assigned to a driver")
                    finally:
                        mycursor.close()
                        connector.close()
        elif(operation_select == "Remove Cab"):
            # calling Cab list
            try:

          
                final_list = get_cabs()
                driver_id = st.selectbox("Select Cab ID",[""]+[[i[0],i[1]] for i in final_list])
                submit_button = st.button("Remove")
                # deleing the selected user
                if(submit_button == True):
                    connector = mysql.connector.connect(
                        host="sql.freedb.tech",
                        user="freedb_shubhanshumishra",
                        password="!ata%t$Fk39QF6!",
                        database="freedb_CabManagment"
                        )
                    mycursor = connector.cursor()
                    sql = "DELETE FROM cabs WHERE cab_registration_number = %s"
                    val = (driver_id[0],)
                    mycursor.execute(sql, val)
                    connector.commit()
                    st.success("Cab Removed Successfully")
            except:
                st.error("Either Cab list is empty or Cab has been assigned to a driver")
        if(operation_select == "Update Cab"):
            st.subheader("Update Cab")
            try:
                final_list = get_cabs()
                cab_id = st.selectbox("Select Cab ID", [""]+[[i[0],i[1]] for i in final_list])
                submit_button = st.button("Search")
                if(len(cab_id) > 1):
                    print(cab_id[0])
                    data = get_cab_specific(cab_id[0])
                    st.write(data)
                    print("_inital")
                    cab_id_new = st.text_input("Enter cab regestration-ID",value = data[0][0],max_chars=20, key="driver_id_new", help="Enter Driver ID")
                    cab_name_new = st.text_input("Enter Cab Model",value = data[0][1],max_chars=50, key="driver_name_new", help="Enter Driver Name")
                    cab_color_new = st.text_input("Enter Cab color",value = data[0][2],max_chars=15, key="driver_email_new", help="Enter Driver Email")
                   
                    submit_button_1 = st.button("Update")
                    if(submit_button_1):
                        print("1")
                        update_cab(cab_id_new,cab_name_new,cab_color_new,cab_id[0])
                        print("2")
                        st.success("Cabs Updated Successfully")

            except:
                st.error("Either Cab list is empty or cab has been assigned to a driver")
    



#=========================== [Managment System] ================================
def add_data(regestration_number, driver_id,driver_name):
        
    connector = mysql.connector.connect(

        host="sql.freedb.tech",
        user="freedb_shubhanshumishra",
        password="!ata%t$Fk39QF6!",
        database="freedb_CabManagment"
        )
    mycursor = connector.cursor()
    sql = "INSERT INTO assignment (cab_registration_number, driver_id,name) VALUES (%s, %s, %s)"
    val = (regestration_number,driver_id,driver_name)
    mycursor.execute(sql, val)
    connector.commit()

def get_data():
    connector = mysql.connector.connect(

        host="sql.freedb.tech",
        user="freedb_shubhanshumishra",
        password="!ata%t$Fk39QF6!",
        database="freedb_CabManagment"
        )
    mycursor = connector.cursor()
    sql = "SELECT * FROM assignment"
    mycursor.execute(sql)
    #connector.commit()
    final_list = []
    for i in mycursor:
        final_list.append(i)
    return final_list

# deleting data
def delete_data(regestration_number, driver_id):
    connector = mysql.connector.connect(

        host="sql.freedb.tech",
        user="freedb_shubhanshumishra",
        password="!ata%t$Fk39QF6!",
        database="freedb_CabManagment"
        )
    mycursor = connector.cursor()
    sql = "DELETE FROM assignment WHERE cab_registration_number = %s AND driver_id = %s"
    val = (regestration_number,driver_id)
    mycursor.execute(sql, val)
    connector.commit()
    


def managment():
    st.subheader("Managment")
    options = st.selectbox("Select Operation", ["","Assign Cab","Remove Assignment"])
    if(options == "Assign Cab"):
        st.subheader("Assign Cab to Driver")
        
        # driver select 
        driver_data = get_driver()
        driver_id = st.selectbox("Select Driver ID",[""]+[[i[1],i[0]] for i in driver_data])
        # cab select
        cab_data = get_cabs()
        cab_id = st.multiselect("Select Cab ID",[""]+[[i[1],i[0]] for i in cab_data])
        submit_button = st.button("Assign")
        if(submit_button):
            print(cab_id)
            try:
                for i in cab_id:
                    add_data(i[1],int(driver_id[1]),driver_id[0])
                st.success("Cab Assigned Successfully")
            except:
                st.error("Cab Already Assigned")
    if(options == "Remove Assignment"):
        data = get_data()
        data = list(set(data))  # removing reduentant data
        with st.expander("View Raw Assignment", expanded = False):
            st.write(data)
        target_data = st.selectbox("select assigment to delete",[""]+[i for i in data])
        if(len(target_data) > 1):
            delete_data(target_data[0],target_data[1])
            st.success("Assignment Deleted Successfully")




                

