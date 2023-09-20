# TASK:1
# # Declare a list variable
# cities = ["Mumbai", "Ayodhya","Jaipur", "Pune", "Nashik"]
# print(cities)
# #  Print the length of the list
# print(len(cities))
#
# # Append a new city to the existing list
# cities.append("Chennai")
# print(cities)
# #  Print the length of the list
# print(len(cities))
#
# # Remove an element at index '2’ from the list and print
# cities.pop(2)
# print(cities)
# print("Process Completed)

# # task:3
# import arcpy
# import os
#
# # Path to file gdb
# file_GDB_path = r"D:\PROG3\assignment_2nd\ProProject_Practical_Two\World_data.gdb"
# fc_name = ["lakes"]
#
# for fc in fc_name:
#     fc_path = os.path.join(file_GDB_path, fc)
#     desc_obj = arcpy.Describe(fc_path)
#
#     sr_obj = desc_obj.spatialReference
#     print(sr_obj.name)
#     print(sr_obj.type)
#
#     shape_type = desc_obj.shapeType
#     print("The geometry type of feature class: {} is {}".format(fc, shape_type))
# field_list = desc_obj.fields
# for field in field_list:
#         print("The field name is {} and the type is {}".format(field.name, field.type))

# task:4
import arcpy

raster_path = r"D:\PROG3\assignment_2nd\ProProject_Practical_Two\RASTER_DATA\erelev"
desc_obj = arcpy.Describe(raster_path)


print(desc_obj.bandCount)


print(desc_obj.format)


print(desc_obj.height)
print(desc_obj.width)
print(desc_obj.basename)
