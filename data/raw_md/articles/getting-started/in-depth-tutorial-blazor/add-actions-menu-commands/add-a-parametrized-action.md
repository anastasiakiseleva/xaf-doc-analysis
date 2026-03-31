---
uid: "402155"
title: Add a Parametrized Action
seealso:
  - linkId: "113711"
  - linkId: "112622"
  - linkId: DevExpress.ExpressApp.Actions.ParametrizedAction
  - linkId: "112621"
---
# Add a Parametrized Action

This lesson explains how to add a **Parametrized Action**. The **Parametrized Action** displays an editor that allows users to type in a parameter value before they run the action. 

The instructions below demonstrate how to add an action that searches for a `DemoTask` object by its `Subject` property value and displays the Detail View of the found object.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402981)
> * [](xref:404256)
> * [](xref:402982)
> * [](xref:402157)


## Step-by-Step Instructions

1. Add a new View Controller to the _MySolution.Module_ project, as described in the [](xref:402157) lesson. Name it _FindBySubjectController_.

2. In the _MySolution.Module_ | _Controllers_ | _FindBySubjectController.cs_ file, specify the controller's properties:

   ```csharp{2,8,10,12}
   // ...
   using MySolution.Module.BusinessObjects;
   // ...
   public partial class FindBySubjectController : ViewController {
       public FindBySubjectController() {
           InitializeComponent();
           // Activate the controller only in the List View.
           TargetViewType = ViewType.ListView;
           // Activate the controller only for root Views.
           TargetViewNesting = Nesting.Root;
           // Specify the type of objects that can use the controller.
           TargetObjectType = typeof(DemoTask);
       }
       // ...
   }
   ```
   [`TargetViewType`]: xref:DevExpress.ExpressApp.ViewController.TargetViewType
   [`TargetViewNesting`]: xref:DevExpress.ExpressApp.ViewController.TargetViewNesting
   [`TargetObjectType`]: xref:DevExpress.ExpressApp.ViewController.TargetObjectType

   For more information about the root View, see the following topic: [](xref:DevExpress.ExpressApp.View.IsRoot).

3. Add a Parametrized Action to the Controller:

   ```csharp{8-13}
   public partial class FindBySubjectController : ViewController {
       public FindBySubjectController() {
           InitializeComponent();
           TargetViewType = ViewType.ListView;
           TargetViewNesting = Nesting.Root;
           TargetObjectType = typeof(DemoTask);

           ParametrizedAction findBySubjectAction =
               new ParametrizedAction(this, "FindBySubjectAction", PredefinedCategory.View, typeof(string)) {
                   ImageName= "Action_Search",
                   NullValuePrompt = "Find task by subject…"
               };
           findBySubjectAction.Execute += FindBySubjectAction_Execute;
       }
   // ...
   }
   ```

   When a user submits a string in the Action's editor, the Action's [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event fires.

4. Handle the Action's `Execute` event to implement custom code:

   ```csharp{6-16}
   public partial class FindBySubjectController : ViewController {
       public FindBySubjectController() {
        // ...
           findBySubjectAction.Execute += FindBySubjectAction_Execute;
       }
       private void FindBySubjectAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
           var objectType = ((ListView)View).ObjectTypeInfo.Type;
           IObjectSpace objectSpace = Application.CreateObjectSpace(objectType);
           string paramValue = e.ParameterCurrentValue as string;
           object obj = objectSpace.FirstOrDefault<DemoTask>(task => task.Subject.Contains(paramValue));
           if(obj != null) {
               DetailView detailView = Application.CreateDetailView(objectSpace, obj);
               detailView.ViewEditMode = ViewEditMode.Edit;
               e.ShowViewParameters.CreatedView = detailView;
           }
       }
   // ...
   }
   ```

   For details on the event handler implementation, refer to the [Detailed Explanation](#detailed-explanation) section.

5. Run the application.

   Select the **Task** item in the navigation control. Type a word from an existing task's `Subject` into the **Find Task by Subject** editor and press Enter. The application displays a detail form with this task.

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor parametrized action|](~/images/blazor_tutorial_parameterized_action.gif)

   Windows Forms

   :   ![|Windows Forms parametrized action|](~/images/blazor_tutorial_parameterized_action_winforms.gif)

## Detailed Explanation

### Search Implementation

In XAF, you use the [Object Space](xref:113707) to query and update persistent objects. Call the static [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method to create an Object Space.

Use the [IObjectSpace.FirstOrDefault\<ObjectType\>](xref:DevExpress.ExpressApp.IObjectSpace.FirstOrDefault*) method to find a `DemoTask` object. This method has the following parameter:

* A lambda expression to search for an object.

### Create a New View

To show the found object in a separate Detail View:
1. Call the [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) method to create a View.
2. Assign the View to the [e.ShowViewParameters.CreatedView](xref:DevExpress.ExpressApp.ShowViewParameters.CreatedView) property of the event parameter. 

> [!TIP]
> You can initialize the `ShowViewParameters` property in the `Execute` event handler of any Action of any type. This allows you to always show a View after an Action is executed. 

For more information on how to show a View in a separate window, refer to the following topic: [Ways to Show a View](xref:112803).

### Manage a Cross-Platform .NET App UI Application

Use [](xref:DevExpress.ExpressApp.XafApplication) object when you need to create a List View, Detail View, Object Space, etc. You can access it from various locations in an XAF application. For example, to access this object from the controller, use the @xref:DevExpress.ExpressApp.Controller.Application property.

[!include[Localization-Overview-Intro](~/templates/coderush-templates-actions-controllers.md)]

## Next Lesson

[](xref:402158)
