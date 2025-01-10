

proyecto_info = {
    "name" : "MyFirstAddon",
    "description" : "Version1",
    "author" : "CarlottaMonath",
    "version" : (0,0,1),
    "blender" : (4,2,1),
    
    "location" : "Desktop > UXProyecto_final",
    "category" : "UX_UI",
}


import bpy
import math
from bpy.types import Menu

addon_keymaps = []

#Implementar un operador que permita al artista mover el origen de un objeto al origen del mundo
class mover_origen_al_origen_del_mundo(bpy.types.Operator):
    bl_idname = "mesh.move_origin_to_world"  # Nomre Operador
    bl_label = "Mover Origen al Mundo"
    bl_options = {"REGISTER", "UNDO"}
    
#Solo funciona en modo Object, por eso el bucle if    
    def execute(self, context):
        print("Executing mover_origen_al_origen_del_mundo")  
        if bpy.context.object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.context.object #context: escena y situacion actual
        bpy.context.scene.cursor.location = (0, 0, 0) #mover 3D-Cursor al origen del muno
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR') #origen del objeto = origen del cursor = origen mundo
        return {'FINISHED'}



# Función para calcular la distancia entre dos puntos
def calcular_distancia(point1, point2):
    """Calcula la distancia euclidiana entre dos puntos."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + 
                     (point2[1] - point1[1]) ** 2 + 
                     (point2[2] - point1[2]) ** 2)

# Operador para calcular la distancia entre el 3D Cursor y el origen del mundo
class CalculateDistanceOperator(bpy.types.Operator):
    bl_idname = "object.calcular_distancia"
    bl_label = "Calcular Distancia"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        cursor_location = context.scene.cursor.location
        origin = (0.0, 0.0, 0.0)  # Origen

        # Cálculo de la distancia
        distancia = calcular_distancia(cursor_location, origin)
        self.report({'INFO'}, f"La distancia del origen a {cursor_location} es: {distancia:.2f}")
        
        return {'FINISHED'}
    
 # Clase para aplicar un material predeterminado a los objetos seleccionados
class AplicarMaterialPredeterminado(bpy.types.Operator):
    bl_idname = "object.aplicar_material_predeterminado"
    bl_label = "Aplicar Material Predeterminado"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        material_name = context.scene.material_name  # Sacar nombre del material de la escena
        material = bpy.data.materials.get(material_name)

        if material is None:
            self.report({'ERROR'}, f"No se encontró el material: {material_name}")
            return {'CANCELLED'}

        # Aplicar el material a todos los objetos seleccionados
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                if obj.data.materials:
                    obj.data.materials[0] = material  # Reemplaza el primer material
                else:
                    obj.data.materials.append(material)  # Añadir un nuevo material

        self.report({'INFO'}, f"Material '{material_name}' aplicado a {len(context.selected_objects)} objeto(s).")
        return {'FINISHED'}
  
 
 
 
 
 
# Clase para rotar un objeto a un ángulo específico
class RotarObjeto(bpy.types.Operator):
    bl_idname = "object.rotar_objeto"  # Nombre del operador
    bl_label = "Rotar Objeto"  # Etiqueta del operador
    bl_options = {"REGISTER", "UNDO"}  # Opciones del operador

    def execute(self, context):
        # Obtener el ángulo de rotación desde la escena
        angle = context.scene.rotation_angle  # Usar el ángulo de rotación de la escena
        radians = math.radians(angle)  # Convertir el ángulo de grados a radianes
            
        # Comprobar si hay un objeto seleccionado
        if context.active_object is not None:
            obj = context.active_object  # Obtener el objeto activo
            
            # Rotar el objeto alrededor del eje Z
            obj.rotation_euler[2] += radians  # Eje Z (rotación en Z)
            
            self.report({'INFO'}, f"Objeto rotado {angle} grados.")  # Mensaje de éxito
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "No hay ningún objeto seleccionado.")  # Mensaje de error
            return {'CANCELLED'}
  

# Clase para copiar objeto     
class CopiarYDistribuirObjeto(bpy.types.Operator):
    bl_idname = "object.copiar_y_distribuir"
    bl_label = "Copiar y Distribuir Objeto"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'ERROR'}, "No hay objeto seleccionado")
            return {'CANCELLED'}

        num_copias = context.scene.num_copias
        distancia = context.scene.distancia_copias

        for i in range(num_copias):
            copia = obj.copy()
            copia.data = obj.data.copy()
            context.collection.objects.link(copia)
            copia.location.x += distancia * (i + 1)

        self.report({'INFO'}, f"Se crearon {num_copias} copias")
        return {'FINISHED'}



# Operador para ajustar la escala de un objeto uniformemente
class AjustarEscalaUniformemente(bpy.types.Operator):
    bl_idname = "object.ajustar_escala_uniformemente"
    bl_label = "Ajustar Escala Uniformemente"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'ERROR'}, "No hay objeto seleccionado")
            return {'CANCELLED'}

        # Usar el factor_escala de la escena
        factor = context.scene.factor_escala
        obj.scale *= factor

        self.report({'INFO'}, f"Escala ajustada por un factor de {factor}")
        return {'FINISHED'}



           
    

class TestPanel( bpy.types.Panel ):
    bl_label = "Herramientas"   #Nombre
    bl_region_type = "UI"       # Zona de la pantalla
    bl_space_type = "VIEW_3D"   # Vista 3D
    bl_category = "Herramientas Artista 3D" # Nombre de la pestaña
    bl_idname = "3D_VIEW_PT_HerramientasArtista3D"
    
    def draw(self, context):
        layout = self.layout #
        row = layout.row() # Nueva fila en el Layout del Panel

        # 1. Origen del Mundo
        layout.label(text="ORIGEN DEL OBJETO AL ORIGEN DEL MUNDO")
        row = layout.row()
        row.operator("mesh.move_origin_to_world", icon="PROP_ON", text="Mover origen del objeto al Mundo")
        layout.separator()

        # 2. Rotación
        layout.label(text="ROTACION")
        row = layout.row()
        row.prop(context.scene, "rotation_angle", text="Ángulo de Rotación")
        row = layout.row()
        row.operator("object.rotar_objeto", icon="DRIVER_ROTATIONAL_DIFFERENCE", text="Rotar Objeto")
        layout.separator()

        # 3. Escala
        layout.label(text="AJUSTAR ESCALA")
        row = layout.row()
        row.prop(context.scene, "factor_escala", text="Factor de Escala")
        row = layout.row()
        row.operator("object.ajustar_escala_uniformemente", icon="FULLSCREEN_ENTER", text="Ajustar Escala")
        layout.separator()

        # 4. Calcular Distancia
        layout.label(text="CALCULAR DISTANCIA")
        row = layout.row()
        row.operator("object.calcular_distancia", icon="TRACKING_FORWARDS_SINGLE", text="Calcular Distancia")
        layout.separator()

        # 5. Copiar y Distribuir
        layout.label(text="COPIAR Y DISTRIBUIR")
        row = layout.row()
        row.prop(context.scene, "num_copias", text="Número de Copias")
        row = layout.row()
        row.prop(context.scene, "distancia_copias", text="Distancia")
        row = layout.row()
        row.operator("object.copiar_y_distribuir", icon="DUPLICATE", text="Copiar y Distribuir")
        layout.separator()

        # 6. Añadir Material
        layout.label(text="AÑADIR MATERIAL")
        row = layout.row()
        row.prop(context.scene, "material_name", text="Nombre del Material")
        row = layout.row()
        row.operator("object.aplicar_material_predeterminado", icon="MATERIAL", text="Aplicar Material Predeterminado")
        
        

#Registrar las clases  

def register(): 
    bpy.utils.register_class( TestPanel ) 
    bpy.utils.register_class( mover_origen_al_origen_del_mundo )
    bpy.utils.register_class( CalculateDistanceOperator )
    bpy.utils.register_class( AplicarMaterialPredeterminado )
    bpy.utils.register_class( RotarObjeto )
    bpy.utils.register_class(CopiarYDistribuirObjeto)
    bpy.utils.register_class(AjustarEscalaUniformemente)
    bpy.utils.register_class(VIEW3D_MT_pie_menu_herramientas)    

    #pie menu
    bpy.types.VIEW3D_MT_editor_menus.append(VIEW3D_MT_pie_menu_herramientas)

    
    bpy.context.area.tag_redraw() 
    
    # Agregar propiedad para el nombre del material en la escena
    bpy.types.Scene.material_name = bpy.props.StringProperty(name="Nombre del Material", default="Material")
    
    
    # Agregar propiedad para el ángulo de rotación en la escena
    bpy.types.Scene.rotation_angle = bpy.props.FloatProperty(name="Ángulo de Rotación", default=0.0)
    
    
    # Agregar propiedad para copiar objetos
    bpy.types.Scene.num_copias = bpy.props.IntProperty(
        name="Número de Copias",
        description="Cantidad de copias a crear",
        default=1,
        min=1,
        max=100
    )
    bpy.types.Scene.distancia_copias = bpy.props.FloatProperty(
        name="Distancia",
        description="Distancia entre copias",
        default=1.0,
        min=0.01
    )
    
    
    # Registrar la propiedad de factor de escala en la escena
    bpy.types.Scene.factor_escala = bpy.props.FloatProperty(
        name="Factor de Escala",
        description="Factor para ajustar la escala uniformemente",
        default=1.0,
        min=0.01,
        max=100.0
    )
    
    # Agregar el atajo de teclado Pie Menu
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("wm.call_menu_pie", 'Q', 'PRESS', ctrl=True, shift=True)
        kmi.properties.name = "VIEW3D_MT_pie_menu_herramientas"
        addon_keymaps.append((km, kmi))
        
        


def unregister(): # Cuando se cierra Blender o el Addon
    bpy.utils.unregister_class( TestPanel )
    bpy.utils.unregister_class( mover_origen_al_origen_del_mundo )
    bpy.utils.unregister_class(CalculateDistanceOperator )
    bpy.utils.unregister_class( AplicarMaterialPredeterminado )
    bpy.utils.unregister_class( RotarObjeto )
    bpy.utils.unregister_class(CopiarYDistribuirObjeto)
    bpy.utils.unregister_class(AjustarEscalaUniformemente)
    bpy.utils.unregister_class(VIEW3D_MT_pie_menu_herramientas) 
    
     # Eliminar la propiedad de la escena
    del bpy.types.Scene.rotation_angle

    #eliminar propiedad de la escena
    del bpy.types.Scene.material_name
    
    # Eliminar la propiedad de factor de escala de la escena
    del bpy.types.Scene.factor_escala
    
    
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    
    
    
    

class VIEW3D_MT_pie_menu_herramientas(Menu):
    bl_label = "Herramientas Artista 3D"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("mesh.move_origin_to_world", text="Mover Origen al Mundo", icon="PROP_ON")
        pie.operator("object.rotar_objeto", text="Rotar Objeto", icon="DRIVER_ROTATIONAL_DIFFERENCE")
        pie.operator("object.ajustar_escala_uniformemente", text="Ajustar Escala", icon="FULLSCREEN_ENTER")
        



if __name__ == "__main__":
    register()
      



