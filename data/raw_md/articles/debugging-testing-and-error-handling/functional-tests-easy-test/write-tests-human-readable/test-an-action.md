---
uid: "113218"
seealso:
- linkId: "113208"
- linkId: "113345"
- linkId: "113294"
title: 'Test an Action'
---
# Test an Action

This topic explains how to test an XAF application. A custom [Controller](xref:112621) that comes with the **Postpone** Action is implemented in this example. Then, this Action's functionality is tested with [EasyTest](xref:113211) functional testing.

![EasyTest_HowToPostponeController](~/images/easytest_howtopostponecontroller116384.png)

## Implement a Custom Action

Create a new custom Controller that will perform an Action over `Task` business objects. The sample `Task` business class exposes two properties - `Description` and `DueDate`.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System;
using System.ComponentModel.DataAnnotations;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace MySolution.Module.BusinessObjects {
    [DefaultClassOptions]
    public class Task : BaseObject {
        public virtual string Description { get; set; }
        public virtual DateTime DueDate { get; set; }
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using System;

namespace MySolution.Module.BusinessObjects {
    [DefaultClassOptions]
    public class Task : BaseObject {
        public Task(Session session) : base(session) { }

        private string description;
        public string Description {
            get => description;
            set => SetPropertyValue(nameof(Description), ref description, value);
        }

        private DateTime dueDate;
        public DateTime DueDate {
            get => dueDate;
            set => SetPropertyValue(nameof(DueDate), ref dueDate, value);
        }
    }
}
```

***

The custom Controller is targeted for [List Views](xref:112611) and contains the **Postpone** Action. This Action processes the selected objects in a `Task` List View. The Action adds one day to the objects' `DueDate` property values.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MySolution.Module.BusinessObjects;
using System;

namespace MySolution.Module.Controllers {
    public class PostponeController : ViewController {
        public PostponeController() {
            TargetObjectType = typeof(Task);
            var postpone = new SimpleAction(this, "Postpone", PredefinedCategory.Edit);
            postpone.SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects;
            postpone.Execute += (s, e) => {
                foreach (object selectedObject in View.SelectedObjects) {
                    Task selectedTask = (Task)selectedObject;
                    selectedTask.DueDate = selectedTask.DueDate == DateTime.MinValue ? DateTime.Today : selectedTask.DueDate.AddDays(1);                    
                }
            };
        }
    }
}
```

***

## Create a Functional Test in a Human-Readable Language

This section describes how to create an EasyTest script that ensures that the implemented **Postpone** Action works as expected.

1. In **Solution Explorer**, navigate to the [module project](xref:118045). Right-click the _FunctionalTests_ folder and select **Add** | **New Item**.
    
    ![EasyTest_HowToPostponeController2](~/images/easytest_howtopostponecontroller2116385.png)
    
    In the **Add New Item** dialog, select **Text File**, set its name to "PostponeControllerTest.ets". Open the newly created file and enter the following code.
    
    # [ETS](#tab/tabid-ets)

    ```ETS
    #DropDB MySolutionEasyTest

    #Application MySolutionWin
    #Application MySolutionWeb
    #Application MySolutionBlazor

    *Action Navigation(Task)

    *Action New

    *FillForm
    Description = Test Task One
    Due Date = 06/06/2011

    *Action Save

    *Action New

    *FillForm
    Description = Test Task Two
    Due Date = 07/07/2011

    *Action Save

    *Action Navigation(Task)

    *SelectRecords
    Columns = Description
    Row = Test Task One
    Row = Test Task Two

    *Action Postpone

    *CheckTable
    Columns = 'Due Date'
    Row = 6/7/2011
    Row = 7/8/2011
    ```
    ***
    
    This script creates two `Task` objects, selects them in the List View and executes the **Postpone** Action. Once ready, the script ensures that the test objects' `DueDate` property values change as expected. For detailed information on the EasyTest command syntax, refer to the [EasyTest Script Reference](xref:113208) topic.
    
    > [!NOTE]
    > By default, the _FunctionalTests_ folder contains the _Sample.ets_ script. You can use it as a starting point when creating tests. If you do not need this file, you can delete it. Another file, initially located in the _FunctionalTests_ folder, is _Config.xml_. This file specifies the  [EasyTest configuration settings](xref:113209) and should not be deleted.
2. Save the test script. 
3. [Run Tests in Console](xref:113210).

