---
uid: "404205"
title: Highlight Property Editors
owner: Anastasiya Kisialeva
---
# Highlight Property Editors

This lesson explains how to format data that satisfies the specified criteria.

The instructions below show how to do the following:

- Add the [Conditional Appearance](xref:113286) module to the application.
- Highlight the **DemoTask** objects whose **Status** property is not set to **Completed**.
- Highlight the **Priority** property when it contains the **High** value.

## Step-by-Step Instructions

1. Add the **DevExpress.ExpressApp.ConditionalAppearance** NuGet package to the _MySolution.Module_ project. See the following topic for more information on how to install DevExpress NuGet packages: [](xref:116042).

2. In the _MySolution.Module_ project, open the _Module.cs_ file and add the Conditional Appearance module:

   ```csharp{9}
   using DevExpress.ExpressApp;
   using DevExpress.ExpressApp.Updating;

   namespace MySolution.Module;

   public sealed class MySolutionModule : ModuleBase {
       public MySolutionModule() {
           // ...
           RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.ConditionalAppearance.ConditionalAppearanceModule));
       }
       //...
   }
   ```	

3. Open the `DemoTask` class and apply the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) attribute as displayed in the code sample below:

   ```csharp{2,5-6}
   // ...
   using DevExpress.ExpressApp.ConditionalAppearance;

   namespace MySolution.Module.BusinessObjects {
       [Appearance("FontColorRed", AppearanceItemType = "ViewItem", TargetItems = "*", 
       Context = "ListView", Criteria = "Status!='Completed'", FontColor = "Red")]
	   [DefaultClassOptions]
	   [ModelDefault("Caption", "Task")]
       public class DemoTask : BaseObject {
	    // ...
       }
   }
   ```

   The first parameter of the `Appearance` attribute is [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Id) --- a unique appearance rule identifier. The rest of the parameters are as follows:
	
   | Parameter | Value | Description |
   |---|---|---|
   | [AppearanceAttribute.AppearanceItemType](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.AppearanceItemType) | `ViewItem` | The appearance rule affects the View Items. |
   | [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems) | `*` | The appearance rule affects all editors and columns. |
   | [AppearanceAttribute.Context](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Context) | `ListView` | The appearance rule is in effect in the `DemoTask` List View. |
   | [AppearanceAttribute.Criteria](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Criteria) | `Status!='Completed'` | The appearance rule affects only uncompleted tasks. |
   | [AppearanceAttribute.FontColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontColor) | `Red` | The color of the affected property text in the UI. |

   > [!NOTE]
   > Follow the [Criteria Language Syntax](xref:4928) rules to specify the `Criteria` value.
    
4. Apply the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) attribute to the `Priority` property of the `DemoTask` class. As the first positional parameter, specify the `Appearance Rule identifier` (e.g., `PriorityBackColorPink`). Then, specify other parameters.

   ```csharp{5-6}
   using DevExpress.ExpressApp.ConditionalAppearance;
   //...
   public class DemoTask : BaseObject {
       // ...
       [Appearance("PriorityBackColorPink", AppearanceItemType = "ViewItem", 
       Context = "Any", Criteria = "Priority=2", BackColor = "255, 240, 240")]
       public virtual Priority Priority { get; set; }
       // ...
   }
   ```
   The first parameter of the `Appearance` attribute is once again [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Id) --- a unique appearance rule identifier. The rest of the parameters are as follows:
	
   | Parameter | Value | Description |
   |---|---|---|
   | [AppearanceAttribute.AppearanceItemType](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.AppearanceItemType) | `ViewItem` | The appearance rule affects the View Items. |
   | [AppearanceAttribute.Context](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Context) | `Any` | The appearance rule is in effect in any View of the `DemoTask` object. |
   | [AppearanceAttribute.Criteria](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Criteria) | `Priority=2` | The appearance rule affects objects with `Priority` property set to `2` (`High`). |
   | [AppearanceAttribute.BackColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.BackColor) | `255, 240, 240` | The color of the affected property field in the UI. |
	
5. Run the application. The `DemoTask` List View and Detail View display a conditional appearance:

   ASP.NET Core Blazor
	
   :   ![|ASP.NET Core Blazor conditional appearance](~/images/tutorial_em_lesson_5_7116957-blazor.png)

   Windows Forms

   :   ![Windows Forms conditional appearance](~/images/tutorial_em_lesson_5_7116957.png)

> [!NOTE]
> You can access these appearance rules from the Model Editor. Open the _Model.DesignedDiffs.xafml_ file and navigate to the **BOModel** | **DemoTask** | **AppearanceRules** node. This node has two child nodes: **FontColorRed** and **PriorityBackColorPink**. XAF generates them automatically from the **Appearance** attributes applied to the `DemoTask` class and the `DemoTask.Priority` property.
> To create a new appearance rule in the Model Editor, add a child node to the **AppearanceRules** node.

## Next Lesson

[](xref:403288)
