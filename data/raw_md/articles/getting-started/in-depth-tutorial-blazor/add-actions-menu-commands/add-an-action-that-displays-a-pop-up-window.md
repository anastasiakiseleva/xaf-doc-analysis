---
uid: "402158"
title: Add an Action that Displays a Pop-Up Window
owner: Alexey Kazakov
seealso:
  - linkId: "113711"
  - linkId: DevExpress.ExpressApp.BaseObjectSpace.SetModified*
  - linkId: "112622"
  - linkId: "112621"
  - linkId: DevExpress.ExpressApp.Actions.PopupWindowShowAction
  - linkId: DevExpress.ExpressApp.SystemModule.DialogController.SaveOnAccept
  - linkId: "404014"
---
# Add an Action that Displays a Pop-Up Window

This lesson explains how to create an Action that shows a pop-up window. This type of Action is useful when users want to input multiple parameters in a pop-up dialog before they execute an Action.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402983)
> * [](xref:402157)

In this tutorial, you will implement the ability to add notes from a predefined list to task descriptions.

## Implement a New Entity

1. Expand the _MySolution.Module_ project and right-click the _Business Objects_ folder. Choose **Add** | **Class…**. Specify _Note.cs_ as the new class name and click **Add**.

2. Replace the generated class declaration with the following code snippet:

    ```csharp
    using DevExpress.ExpressApp.DC;
    using DevExpress.Persistent.Base;
    using System.ComponentModel;
    using System.ComponentModel.DataAnnotations;

    namespace MySolution.Module.BusinessObjects;

    [DefaultProperty(nameof(Text))]
    [ImageName("BO_Note")]
    public class Note {

        [Key, Browsable(false)]
        [DevExpress.ExpressApp.Data.Key]
        [HideInUI(HideInUI.All)]
        public virtual Guid ID { get; set; }
        public virtual String Author { get; set; }
        public virtual DateTime? DateTime { get; set; }

        [FieldSize(FieldSizeAttribute.Unlimited)]
        public virtual String Text { get; set; }
    }
    ```

3. Register the `Note` type in `DbContext`. Edit the _BusinessObjects\MySolutionDbContext.cs_ file as shown below:
	
   ```csharp{3}
   public class MySolutionEFCoreDbContext : DbContext {
       // ...
       public DbSet<Note> Notes { get; set; }
   }
   ```

## Create a View Controller

1. Add a new View Controller to the **MySolution.Module** project. Name it _PopupNotesController_.
2. In the _PopupNotesController.cs_ file, specify the controller properties:

   ```csharp{9-10}
   using DevExpress.ExpressApp;
   using MySolution.Module.BusinessObjects;
   // ...
   public partial class PopupNotesController : ViewController {
       // ...
       public PopupNotesController() {
           InitializeComponent();
           //Target the required Views and create their Actions
           TargetObjectType = typeof(DemoTask);
           TargetViewType = ViewType.DetailView;
       }
       // ...
   }
   ```

3. Add the `ShowNotesAction` action and handle its `CustomizePopupWindowParams` event:

   ```csharp{8-12,15-18}
   public partial class PopupNotesController : ViewController {
       public PopupNotesController() {
           InitializeComponent();
           TargetObjectType = typeof(DemoTask);
           TargetViewType = ViewType.DetailView;
           /*Invoke a pop-up window with a specified View and execute custom code
             when a user clicks the OK or Cancel button.*/
           PopupWindowShowAction showNotesAction = new PopupWindowShowAction(this, "ShowNotesAction", PredefinedCategory.Edit) {
               Caption = "Show Notes"
           };

           showNotesAction.CustomizePopupWindowParams += ShowNotesAction_CustomizePopupWindowParams;
       }

       private void ShowNotesAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
           //Create a List View for Note objects in the pop-up window.
           e.View = Application.CreateListView(typeof(Note), true);
       }
       // ...
   }
   ```
   [`PopupWindowShowAction`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction
   [`CustomizePopupWindowParams`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams

4. Add and handle the `ShowNotesAction`'s `Execute` event. It occurs when a user clicks **OK** in the pop-up window. The event handler code appends the `Note.Text` property value to the `Task.Description` property value.

   ```csharp{4,7-17}
   // ...
   public PopupNotesController() {
       // ...
       showNotesAction.Execute += ShowNotesAction_Execute;
   }

   private void ShowNotesAction_Execute(object sender, PopupWindowShowActionExecuteEventArgs e) {
       DemoTask task = (DemoTask)View.CurrentObject;
       foreach(Note note in e.PopupWindowViewSelectedObjects) {
           if(!string.IsNullOrEmpty(task.Description)) {
               task.Description += Environment.NewLine;
           }
           // Add selected note texts to a Task's description
           task.Description += note.Text;
       }
       View.ObjectSpace.CommitChanges();
   }
   ```
   
   The event handler's [e.PopupWindowViewSelectedObjects](xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs.PopupWindowViewSelectedObjects) parameter provides an object that a user selects in the pop-up window.

5. Run the application. 

   Open a **Task** item's Detail View. The Detail View toolbar displays the **Show Notes** button. This is the action implemented in this lesson.

   Click the button to open the pop-up window. The pop-up window displays a list view for the **Note** objects. Create a **Note** object.

   Click this **Note** object in the list. The `Task.Description` property value should change.

   ASP.NET Core Blazor

   :   ![ASP.NET Core Blazor pop-up window action](~/images/blazor-tutorial-popupwindowaction.gif)

   Windows Forms

   :   ![Windows Forms pop-up window action](~/images/blazor-tutorial-popupwindowaction-winforms.gif)

For an example of how to create and show a Detail View, refer to the following topic: [How to: Create and Show a Detail View of the Selected Object in a Popup Window](xref:118760).

[!include[Localization-Overview-Intro](~/templates/coderush-templates-actions-controllers.md)]

## Next Lesson

[](xref:402159)
