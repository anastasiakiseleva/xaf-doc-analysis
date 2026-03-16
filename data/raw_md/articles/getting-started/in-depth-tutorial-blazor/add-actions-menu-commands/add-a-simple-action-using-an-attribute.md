---
uid: "402156"
title: Add a Simple Action Using an Attribute
owner: Alexey Kazakov
seealso:
  - linkId: "112621"
  - linkId: "112622"
  - linkId: DevExpress.Persistent.Base.ActionAttribute
  - linkId: "404559#use-actionattribute-to-add-an-inline-action-to-a-list-view-grid"
    altText: Use ActionAttribute to Add an Inline Action to a List View Grid
---
# Add a Simple Action Using an Attribute

This lesson explains how to use methods of an entity class to add a Simple Action.

The instructions below show how to add a new method with the [](xref:DevExpress.Persistent.Base.ActionAttribute) attribute to the `DemoTask` class.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402983)
> * [](xref:402157)

## Step-by-Step Instructions

1. Add the `Postpone` method to the `DemoTask` class:
    
   ```csharp{9,11-16}
   namespace MySolution.Module.BusinessObjects

   [DefaultClassOptions]
   [ModelDefault("Caption", "Task")]
   public class DemoTask : BaseObject {
       // ...
       /* Use this attribute to display the Postpone button in the UI
       and call the Postpone() method when a user clicks this button*/
       [Action(ToolTip = "Postpone the task to the next day", Caption = "Postpone")]
       // Shift the task's due date forward by one day
       public void Postpone() {
           if(DueDate == DateTime.MinValue) {
               DueDate = DateTime.Now;
           }
           DueDate = DueDate + TimeSpan.FromDays(1);
       }
   }
   ```
   [`Action`]: xref:DevExpress.Persistent.Base.ActionAttribute

   > [!TIP]
   > You can use the `Action` attribute to implement an action that asks a user to specify parameters in a popup dialog (for example, the number of days to postpone a **Task**). Refer to the following topic for an example: [How to: Create an Action Using the Action Attribute](xref:112619).

2. Run the application. Select the **Task** item in the navigation control. 
    
   Select one or more tasks in the **Task** List View. This activates the **Postpone** Action button. Click this button to shift the due date of the selected tasks forward by one day.

   ASP.NET Core Blazor
    
   :   ![|ASP.NET Core Blazor attribute action postpone|](~/images/blazor-tutorial-attribute-action-postpone.gif)

   Windows Forms

   :   ![|Windows Forms attribute action postpone|](~/images/blazor-tutorial-attribute-action-postpone-winforms.gif)

[!include[Localization-Overview-Intro](~/templates/coderush-templates-actions-controllers.md)]
    
## Next Lesson

[](xref:402131)
