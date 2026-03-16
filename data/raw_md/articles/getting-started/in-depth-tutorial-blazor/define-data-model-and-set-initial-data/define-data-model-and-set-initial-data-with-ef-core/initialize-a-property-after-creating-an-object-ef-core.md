---
uid: "402982"
title: Initialize Entity Properties
owner: Alexey Kazakov
seealso:
  - linkId: "112570"
  - linkId: "112701"
  - linkId: "113258"
---
# Initialize Entity Properties

This lesson explains how to initialize properties in the newly created entity instances. 

The steps below show how to add a `Priority` property to the `DemoTask` class and how to initialize the property value. For `DemoTask` class implementation code, see the following lesson: [Set a Many-to-Many Relationship](xref:402983).

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402981)
> * [](xref:402983)

## Step-by-Step Instructions

1. Add the `Priority` property to the `DemoTask` class and declare the `Priority` enumeration:
    
    ```csharp
    namespace MySolution.Module.BusinessObjects {
        //...
        public class DemoTask : BaseObject {
            //...
            public virtual Priority Priority { get; set; }
        }

        public enum Priority {
            Low = 0,
            Normal = 1,
            High = 2
        }
    }
    ```

2. Use the code below to initialize the newly added `Priority` property when you create a `DemoTask` object:
    
    ```csharp
    public class DemoTask : BaseObject {
        //..
        public override void OnCreated() {
            Priority = Priority.Normal;
        }
        //...
    }
    ```
    
3. Run the application. 

   Create a new `Task` object. In the Task detail view, the `Priority` field value is `Normal`, as you declared in the code above.

   ASP.NET Core Blazor
    
   :   ![|ASP.NET Core Blazor initialize property value|](~/images/tutorial_bmd_lesson12.png)

   Windows Forms

   :   ![Windows Forms initialize property value](~/images/task-initialized-property-winforms.png)

   Note that XAF generates a combo box for the `Priority` property. The combo box items are the enumeration values you declared in step 1.

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor enumeration combo box|](~/images/btutor_bmd_combobox_for_enum.png)

   Windows Forms

   :   ![Windows Forms enumeration combo box](~/images/task-priority-combobox-winforms.png)

## Next Lesson

[](xref:402979)