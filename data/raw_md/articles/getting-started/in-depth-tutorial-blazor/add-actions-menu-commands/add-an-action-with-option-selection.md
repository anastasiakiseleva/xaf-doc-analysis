---
uid: "402159"
title: Add an Action with Option Selection
seealso:
  - linkId: "113711"
  - linkId: DevExpress.ExpressApp.BaseObjectSpace.CommitChanges
  - linkId: "112792"
  - linkId: "112621"
  - linkId: DevExpress.ExpressApp.Actions.SingleChoiceAction
  - linkId: "112622"
---
# Add an Action with Option Selection

This lesson explains how to create an Action that supports option selection. 

In this lesson, you will implement a new View Controller with a `SingleChoiceAction`. This action will allow users to select values for the `Task.Priority` and `Task.Status` properties.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402157)
> * [](xref:402158)

## Step-by-Step Instructions

1. Add a new View Controller to the _MySolution.Module_ project. Name it _TaskActionsController_.
2. In the _TaskActionsController.cs_ file, set the controller's `TargetObjectType`:
     
   ```csharp{7}
   using DevExpress.ExpressApp;
   using MySolution.Module.BusinessObjects;
   // ...
   public partial class TaskActionsController : ViewController {
       public TaskActionsController() {
           InitializeComponent();
           TargetObjectType = typeof(DemoTask);
       }
       // ...
   }
   ```

3. Add a `SingleChoiceAction` and specify its properties:

   ```csharp{6-12}
   public partial class TaskActionsController : ViewController {
       public TaskActionsController() {
           InitializeComponent();
           TargetObjectType = typeof(DemoTask);

           SingleChoiceAction SetTaskAction = new SingleChoiceAction(this, "SetTaskAction", PredefinedCategory.Edit) {
               Caption = "Set Task",
               //Specify the display mode for the Action's items. Here the items are operations that you perform against selected records.
               ItemType = SingleChoiceActionItemType.ItemIsOperation,
               //Set the Action to become available in the Task List View when a user selects one or more objects.
               SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects
           };
       }
       // ...
   }

   ```
   [`SingleChoiceActionItemType`]: xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType
   [`SelectionDependencyType`]: xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType

4. To populate the Action with items, fill the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection in the Controller's constructor:
    
   ```csharp{2-3,6-9,11-14,17-24}
   public partial class TaskActionsController : ViewController {
      private ChoiceActionItem setPriorityItem;
      private ChoiceActionItem setStatusItem;
      public TaskActionsController() {
         // ...
         setPriorityItem = 
            new ChoiceActionItem(CaptionHelper.GetMemberCaption(typeof(DemoTask), "Priority"), null);
         SetTaskAction.Items.Add(setPriorityItem);
         FillItemWithEnumValues(setPriorityItem, typeof(Priority));
          
         setStatusItem = 
            new ChoiceActionItem(CaptionHelper.GetMemberCaption(typeof(DemoTask), "Status"), null);
         SetTaskAction.Items.Add(setStatusItem);
         FillItemWithEnumValues(setStatusItem, typeof(BusinessObjects.TaskStatus));
        
      }
      private void FillItemWithEnumValues(ChoiceActionItem parentItem, Type enumType) {
           EnumDescriptor ed = new EnumDescriptor(enumType);
           foreach(object current in ed.Values) {
               ChoiceActionItem item = new ChoiceActionItem(ed.GetCaption(current), current);
               item.ImageName = ImageLoader.Instance.GetEnumValueImageName(current);
               parentItem.Items.Add(item);
           }
       }
   }
   ```

   The code sample above organizes items from the Action's `Items` collection as a tree:

   * The root level contains items whose captions correspond to the `DemoTask.Priority` and `DemoTask.Status` property names. The [](xref:DevExpress.ExpressApp.Utils.CaptionHelper) object returns item captions. 
   * The nested level contains the `Priority` and `Status` enumeration values. The @DevExpress.ExpressApp.Utils.EnumDescriptor object returns item captions.

   ASP.NET Core Blazor

   :   ![|option selection action tree items](~/images/blazor-tutorial-option-selection-action-tree-items.png)

   Windows Forms

   :   ![|option selection action tree items](~/images/blazor-tutorial-option-selection-action-tree-items-winforms.png)

   When you populate the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection in a Controller constructor as shown in the code above, you can use the [Model Editor](xref:112830)'s [!include[Node_Action](~/templates/node_action111373.md)] | **ChoiceActionItems** node to set an image name, a shortcut, and a localized caption for the added items. 

   If you populate the `Items` collection in a [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler, the Model Editor does not load items.
    
5. Open the _DemoTask.cs_ file and assign images to the `Priority` enumeration value as in the code sample below:
    
   ```csharp
   public enum Priority {
       [ImageName("State_Priority_Low")]
       Low,
       [ImageName("State_Priority_Normal")]
       Normal,
       [ImageName("State_Priority_High")]
       High
   }
   ```

   In this tutorial, the enumeration values have the [](xref:DevExpress.Persistent.Base.ImageNameAttribute) attributes to set images for these values in the UI.

   XAF ships with the standard image library. The library includes the `State_Priority_Low`, `State_Priority_Normal` and `State_Priority_High` images used in this lesson.
    
6. Handle the [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event that occurs when a user chooses the Action's item:
    
   ```csharp{2,8,10-30}
   //...
   using System.Collections;

   public partial class TaskActionsController : ViewController {
       // ...
       public TaskActionsController() {
           // ...
           SetTaskAction.Execute += SetTaskAction_Execute;
       }    
       private void SetTaskAction_Execute(object sender, SingleChoiceActionExecuteEventArgs e) {
           /*Create a new ObjectSpace if the Action is used in List View.
             Use this ObjectSpace to manipulate the View's selected objects.*/
           IObjectSpace objectSpace = View is ListView ?
               Application.CreateObjectSpace(typeof(DemoTask)) : View.ObjectSpace;
           ArrayList objectsToProcess = new ArrayList(e.SelectedObjects);
           if(e.SelectedChoiceActionItem.ParentItem == setPriorityItem) {
               foreach(Object obj in objectsToProcess) {
                   DemoTask objInNewObjectSpace = (DemoTask)objectSpace.GetObject(obj);
                   objInNewObjectSpace.Priority = (Priority)e.SelectedChoiceActionItem.Data;
               }
           } else
               if(e.SelectedChoiceActionItem.ParentItem == setStatusItem) {
               foreach(Object obj in objectsToProcess) {
                   DemoTask objInNewObjectSpace = (DemoTask)objectSpace.GetObject(obj);
                   objInNewObjectSpace.Status = (BusinessObjects.TaskStatus)e.SelectedChoiceActionItem.Data;
               }
           }
           objectSpace.CommitChanges();
           View.ObjectSpace.Refresh();
       }
   }    
   ```

   To access a selected action item, use the event handler's [e.SelectedChoiceActionItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceActionExecuteEventArgs.SelectedChoiceActionItem) parameter.

   Create a separate `ObjectSpace` to edit multiple objects that are currently displayed. This technique improves performance, as each object change does not trigger the grid control's events.

7. Run the application. Select the **Task** item in the navigation control. After that, the **Set Task** Action becomes active. 

   To change the `Priority` or `Status` property of the selected `Task` object, select an item in the Action's drop-down list:

   ASP.NET Core Blazor
    
   :   ![|ASP.NET Core Blazor action option selection in detail view|](~/images/btutorial_ef_lesson5_3.png)

   Windows Forms

   :   ![|ASP.NET Core Blazor action option selection in detail view|](~/images/btutorial_ef_lesson5_3_winforms.png)

[!include[Localization-Overview-Intro](~/templates/coderush-templates-actions-controllers.md)]

## Next Lesson

[](xref:402156)
