---
uid: DevExpress.ExpressApp.XafApplication.ResourcesExportedToModel
name: ResourcesExportedToModel
type: Property
summary: Provides access to a collection of Resource Localizers used in the current application to extend the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelLocalization) node.
syntax:
  content: public List<Type> ResourcesExportedToModel { get; set; }
  parameters: []
  return:
    type: System.Collections.Generic.List{System.Type}
    description: An **IList\<Type>** collection of Resource Localizer types.
seealso:
- linkId: DevExpress.ExpressApp.ModuleBase.GetXafResourceLocalizerTypes
---
The most recommended way to localize your application is described in the [How to: Localize an XAF Application](xref:402956) topic.

By default, the **Localization** node allows you to localize internal XAF resources only. However, you can extend this node with child nodes that will allow you to localize the resource strings of the required control used in your application. There are several ways to do this:

* **In code**
    
    Add the required Resource Localizers to the collection returned by the **ResourcesExportedToModel** property.
    
    In a Windows Forms application:
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    public class Program {
       public static void Main(string[] arguments) {
          MySolutionWinApplication winApplication = new MySolutionWinApplication();
          //...      
          winApplication.ResourcesExportedToModel.Add(typeof(
             DevExpress.ExpressApp.Win.Localization.GridControlLocalizer));
          winApplication.Setup();
          //...
       }
    }
    ```
    ***

Invoke the [Model Editor](xref:112830) for the current application project. In the **Localization** node, you will find child nodes corresponding to the added resources. Here, you can localize them, as with any other resources in XAF (see [Localization Basics](xref:112595) and [Localize UI Elements](xref:403184)):

![ResourceLocalizers_Model](~/images/resourcelocalizers_model116199.png)

To learn how to use a ready-to-use satellite assembly with strings translated to the required language, refer to the [Localize Standard XAF Modules and DevExpress Controls Used in an Application](xref:113301) topic.