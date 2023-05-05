import Utilities as Ut
import matplotlib.pyplot as plt

age_range = {"Adulto Joven": 18, "Adulto":30, "Adulto Mayor":60}
bmi_range = {"Bajo Peso":18.5, "Peso Normal": 25, "Sobre-peso":30, "Obesidad":40}

Data = Ut.ReadCSV_Dict("insurance.csv", [1,0,2,1,0,0,2])
n_top = 100
Top_Cost_Expensive = Ut.Top(list_top=Data, n_top = n_top, key_sort = "charges", rev=True)
Top_Cost_Cheap = Ut.Top(list_top = Data, n_top = n_top, key_sort = "charges")

Exp_charge = Top_Cost_Expensive[0]
Che_charge = Top_Cost_Cheap[0]

print("Valores de la persona con costo mas caro en el seguro")
for k, v in Exp_charge.items():
    print("{k} : {v}".format(k=k, v=v))

print("Valores de la persona con costos mas barato en el seguro")
for k, v in Che_charge.items():
    print("{k} : {v}".format(k=k, v=v))

#Fumadores en el top mas caro
Smokers_exp = sum([1 for element in Top_Cost_Expensive if element["smoker"]=="yes"])
NoSmokers_exp = sum([1 for element in Top_Cost_Expensive if element["smoker"]=="no"])

#Fumadores en el top mas barato
Smokers_che = sum([1 for element in Top_Cost_Cheap if element["smoker"]=="yes"])
NoSmokers_che = sum([1 for element in Top_Cost_Cheap if element["smoker"]=="no"])


plt.pie([Smokers_exp,NoSmokers_exp],labels = ["Smokers","No Smokers"])
plt.title("Personas Fumadoras en Top {n} de costos mas caros".format(n=n_top))
plt.legend(labels=["Smokers","No Smokers"], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=2)
plt.show()

plt.pie([Smokers_che, NoSmokers_che], labels = ["Smokers","No Smokers"])
plt.title("Personas Fumadoras en Top {n} de costos mas baratos".format(n=n_top))
plt.legend(labels=["Smokers","No Smokers"], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=2)
plt.show()

#Expensive
Exp_Ages = {"Adulto Joven":0, "Adulto":0, "Adulto Mayor":0}

Exp_Ages["Adulto Joven"] = sum([1 for element in Top_Cost_Expensive if element["age"]>=age_range["Adulto Joven"] and element["age"]<age_range["Adulto"]])
Exp_Ages["Adulto"] = sum([1 for element in Top_Cost_Expensive if element["age"]>=age_range["Adulto"] and element["age"]<age_range["Adulto Mayor"]])
Exp_Ages["Adulto Mayor"] = sum([1 for element in Top_Cost_Expensive if element["age"]>=age_range["Adulto Mayor"]])

#Cheap
Che_Ages = {"Adulto Joven":0, "Adulto":0, "Adulto Mayor":0}

Che_Ages["Adulto Joven"] = sum([1 for element in Top_Cost_Cheap if element["age"]>=age_range["Adulto Joven"] and element["age"]<age_range["Adulto"]])
Che_Ages["Adulto"] = sum([1 for element in Top_Cost_Cheap if element["age"]>=age_range["Adulto"] and element["age"]<age_range["Adulto Mayor"]])
Che_Ages["Adulto Mayor"] = sum([1 for element in Top_Cost_Cheap if element["age"]>=age_range["Adulto Mayor"]])


plt.pie([i for i in Exp_Ages.values()],labels = list(Exp_Ages.keys()))
plt.title("Rango de Edades para el Top {n} mas caros".format(n=n_top))
plt.legend(labels=[i for i in Exp_Ages.keys()], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=len(Exp_Ages))
plt.show()

plt.pie([i for i in Che_Ages.values()],labels = list(Che_Ages.keys()))
plt.title("Rango de Edades para el Top {n} mas baratos".format(n=n_top))
plt.legend(labels=[i for i in Che_Ages.keys()], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=len(Che_Ages))
plt.show()


# Rangos de BMI
Exp_bmi = {"Bajo Peso":0, "Peso Normal": 0, "Sobre-peso":0, "Obesidad":0, "Obesidad Morbida":0}
Che_bmi = {"Bajo Peso":0, "Peso Normal": 0, "Sobre-peso":0, "Obesidad":0, "Obesidad Morbida":0}

Exp_bmi["Bajo Peso"] = sum([1 for element in Top_Cost_Expensive if element["bmi"]<bmi_range["Bajo Peso"]])
Exp_bmi["Peso Normal"] = sum([1 for element in Top_Cost_Expensive if element["bmi"]>=bmi_range["Bajo Peso"] and element["bmi"]<bmi_range["Peso Normal"]])
Exp_bmi["Sobre-peso"] = sum([1 for element in Top_Cost_Expensive if element["bmi"]>=bmi_range["Peso Normal"] and element["bmi"]<bmi_range["Sobre-peso"]])
Exp_bmi["Obesidad"] = sum([1 for element in Top_Cost_Expensive if element["bmi"]>=bmi_range["Sobre-peso"] and element["bmi"]<bmi_range["Obesidad"]])
Exp_bmi["Obesidad Morbida"] = sum([1 for element in Top_Cost_Expensive if element["bmi"]>=bmi_range["Obesidad"]])

Che_bmi["Bajo Peso"] = sum([1 for element in Top_Cost_Cheap if element["bmi"]<bmi_range["Bajo Peso"]])
Che_bmi["Peso Normal"] = sum([1 for element in Top_Cost_Cheap if element["bmi"]>=bmi_range["Bajo Peso"] and element["bmi"]<bmi_range["Peso Normal"]])
Che_bmi["Sobre-peso"] = sum([1 for element in Top_Cost_Cheap if element["bmi"]>=bmi_range["Peso Normal"] and element["bmi"]<bmi_range["Sobre-peso"]])
Che_bmi["Obesidad"] = sum([1 for element in Top_Cost_Cheap if element["bmi"]>=bmi_range["Sobre-peso"] and element["bmi"]<bmi_range["Obesidad"]])
Che_bmi["Obesidad Morbida"] = sum([1 for element in Top_Cost_Cheap if element["bmi"]>=bmi_range["Obesidad"]])


plt.pie([i for i in Exp_bmi.values()],labels = list(Exp_bmi.keys()))
plt.title("Rango de BMI(IMC) para el Top {n} mas caros".format(n=n_top))
plt.legend(labels=[i for i in Exp_bmi.keys()], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=len(Exp_bmi))
plt.show()

plt.pie([i for i in Che_bmi.values()],labels = list(Che_bmi.keys()))
plt.title("Rango de BMI(IMC) para el Top {n} mas baratos".format(n=n_top))
plt.legend(labels=[i for i in Che_bmi.keys()], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=len(Exp_bmi))
plt.show()


#Hombres y Mujeres

Exp_Gen = {"Mujer":0, "Hombre":0}
Che_Gen = {"Mujer":0, "Hombre":0}

Exp_Gen["Mujer"] = sum([1 for i in Top_Cost_Expensive if i["sex"]=="female"])
Exp_Gen["Hombre"] = sum([1 for i in Top_Cost_Expensive if i["sex"]=="male"])

Che_Gen["Mujer"] = sum([1 for i in Top_Cost_Cheap if i["sex"]=="female"])
Che_Gen["Hombre"] = sum([1 for i in Top_Cost_Cheap if i["sex"]=="male"])

plt.pie([i for i in Exp_Gen.values()],labels = list(Exp_Gen.keys()))
plt.title("Rango de BMI(IMC) para el Top {n} mas caros".format(n=n_top))
plt.legend(labels=[i for i in Exp_Gen.keys()], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=len(Exp_Gen))
plt.show()

plt.pie([i for i in Che_Gen.values()],labels = list(Che_Gen.keys()))
plt.title("Rango de BMI(IMC) para el Top {n} mas baratos".format(n=n_top))
plt.legend(labels=[i for i in Exp_Gen.keys()], loc = "upper center", bbox_to_anchor = (0.5, -0.04), ncol=len(Exp_Gen))
plt.show()