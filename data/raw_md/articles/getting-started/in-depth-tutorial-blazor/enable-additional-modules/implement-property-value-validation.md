---
uid: "402980"
title: Implement Property Value Validation
owner: Alexey Kazakov
seealso:
  - linkId: "113684"
---

# Implement Property Value Validation

This lesson explains how to set validation rules for entity classes and their properties. XAF applies these rules when a user executes a specific operation (for example, saves an edited object).

The Validation System offers a number of predefined rule types and contexts. A rule specifies a data validity condition. A context defines the moment when the application checks the rule.

To use XAF Validation functionality, you need the `DevExpress.ExpressApp.Validation.Blazor` and `DevExpress.ExpressApp.Validation.Win` NuGet packages. When you created the solution and selected the **Validation** module in the project wizard, the wizard added these packages to platform-specific projects.

> [!TIP]
>
> To add this functionality to an existing application, you need to install the NuGet packages and register the modules. For additional information, refer to the following section: [Validation System Elements](xref:113684#validation-system-elements).

The instructions below explain how to do the following:

- Use the [Model Editor](xref:112582) to prevent a user from marking a task as completed before the task starts (`DemoTask.Status` is `NotStarted`).
- Create a rule in code that requires that the `Position.Title` property must not be empty.

## Implement Property Value Validation in Model Editor

1. Open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582). Navigate to the **Validation** | **Rules** node. Right-click the **Rules** node and select **Add…** | **RuleCriteria**.
    
   ![|Validation in Model Editor|](~/images/blazor_tutorial_uic_validation.png)

2. Set values of the following properties for the node:

   * **TargetType** to `MySolution.Module.BusinessObjects.DemoTask`
   * **Criteria** to `Status != 'NotStarted'`
   * **ID** to `TaskStarted`
   * **TargetContextIDs** to `MarkCompleted`
   * **CustomMessageTemplate** to `Cannot set the task as completed because it has not started.`
    
   ![|XAF ASP.NET Core Blazor validation in model editor|](~/images/blazor_tutorial_uic_validation_settings.png)

   The **Criteria** property value must respect the [Criteria Language Syntax](xref:4928). To set the criteria, click the ellipsis button to the right of the **Criteria** value and invoke the **Filter Builder** dialog. In this dialog, you can visually design a criteria expression.
    
3. Navigate to the **ActionDesign** | **Actions** | **DemoTask.MarkCompleted** node and set the **ValidationContexts** property to `MarkCompleted`.
    
   ![|Tutorial_UIC_Lesson14_2_1|](~/images/blazor_tutorial_uic_validation_context.png)

4. Change the caption of the **MarkCompleted** Action to `Mark Completed`.

5. Run the application and go to one of the unfinished tasks. Click the **Mark Completed** button. The following **Validation Error** dialog appears:

   ASP.NET Core Blazor
    
   :   ![|ASP.NET Core Blazor validation error message|](~/images/blazor_tutorial_uic_validation_error_message.png)

   Windows Forms

   :   ![|Windows Forms validation error message|](~/images/blazor_tutorial_uic_validation_error_message-winforms.png)

## Implement Property Value Validation in Code

1. Apply the `RuleRequiredField` attribute to the `Title` property in the `Position` class. Specify the context that triggers the rule (for example, `DefaultContexts.Save`) as the attribute's parameter:
    
    ```csharp{2,11}
    // ...
    using DevExpress.Persistent.Validation;

    //...
    {
        [DefaultClassOptions]
        [DefaultProperty(nameof(Title))]
        public class Position : BaseObject {
            /*Define a validation rule that ensures that the `Position.Title` property
              has a value when you save the `Position` object.*/
            [RuleRequiredField(DefaultContexts.Save)]
            public virtual string Title { get; set; }
            //...
        }
    }
    ```
    [`RuleRequiredField`]: xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute
    
    ***    

2. Run the application and go to the **Position** List View. 
    
   Click the **New** button to create a new **Position** object. Leave the `Title` property empty and click **Save**. The following **Validation Error** dialog appears:

   ASP.NET Core Blazor
    
   :   ![|XAF ASP.NET Core Blazor validation|](~/images/tutorial-blazor-buildmodel-validation.png)

   Windows Forms

   :   ![|XAF ASP.NET Core Blazor validation|](~/images/tutorial-blazor-buildmodel-validation-winforms.png)

## Next Lesson

[](xref:404205)
