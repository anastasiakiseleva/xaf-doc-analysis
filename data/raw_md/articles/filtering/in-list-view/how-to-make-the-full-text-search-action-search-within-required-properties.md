---
uid: "112923"
seealso:
- linkId: DevExpress.ExpressApp.Frame.GetController``1
title: 'How to: Make the FullTextSearch Action Search Within Required Properties'
owner: Ekaterina Kiseleva
---
# How to: Make the FullTextSearch Action Search Within Required Properties

This topic demonstrates how to customize the **FullTextSearch** Action's behavior. This Action filters the current List View by setting criteria for its collection data source. According to the criteria, the object's properties must contain individual words from the word combination typed by an end-user. Reference several techniques on how to modify the Action's behavior, in the [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) member description. Here, you will see how to use one of these techniques. We will specify a custom list of the properties that will be used to generate the filter criterion for the current List View.

To specify a custom list of the properties that will be used in the search, the Filter Controller, which contains the **FullTextSearch** Action, exposes the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event. To handle this event, we will add a new [View Controller](xref:112621), and subscribe to its [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event.

In the **CustomGetFullTextSearchProperties** event handler, assign a list of any required properties to the [CustomGetFullTextSearchPropertiesEventArgs.Properties](xref:DevExpress.ExpressApp.SystemModule.CustomGetFullTextSearchPropertiesEventArgs.Properties) parameter. In addition, set the **CustomGetFullTextSearchPropertiesEventArgs.Handled** parameter to **true**, to indicate that other properties must not be added to the list. In this example, we will add only the "LastName" property of the Person class. So, we will activate our Controller for Person List Views only. The **MyFilterController** is shown below:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Collections.Generic;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
//...
public class MyFilterController : ViewController {
    public MyFilterController() {
        TargetObjectType = typeof(MySolution.Module.BusinessObjects.Person);
    }
    private FilterController standardFilterController;
    protected override void OnActivated() {
        base.OnActivated();
        standardFilterController = Frame.GetController<FilterController>();
        if(standardFilterController != null) {
            standardFilterController.CustomGetFullTextSearchProperties += standardFilterController_CustomGetFullTextSearchProperties;
        }
    }
    void standardFilterController_CustomGetFullTextSearchProperties(object sender, 
CustomGetFullTextSearchPropertiesEventArgs e) {
        foreach(string property in GetFullTextSearchProperties()) {
            e.Properties.Add(property);
        }
        e.Handled = true;
    }
    private List<string> GetFullTextSearchProperties() {
        List<string> searchProperties = new List<string>();
        searchProperties.Add("LastName");
        return searchProperties;
    }
    protected override void OnDeactivated() {
        if (standardFilterController != null) {
            standardFilterController.CustomGetFullTextSearchProperties -= standardFilterController_CustomGetFullTextSearchProperties;
        }
        base.OnDeactivated();
    }
}
```
***

The following image demonstrate that the **MyFilterController** works:

![FilterByTextAction_CustomGetFullTextSearchProperties](~/images/filterbytextaction_customgetfulltextsearchproperties116300.png)

Filtration may be impossible in case one or more property is of a particular type. For example, in [Server](xref:118450) mode, filtering by properties of the [DateTime](https://learn.microsoft.com/en-us/dotnet/api/system.datetime) type, which are stored in a database as columns of the [datetime](https://learn.microsoft.com/en-us/sql/t-sql/data-types/datetime-transact-sql) date type, may cause exceptions. To avoid them, ensure that the entered text can be converted to the corresponding type and this converted value is within the acceptable range, and exclude a property from the default filter list if necessary. The following code demonstrates the Controller implementing this logic.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Collections.Generic;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.DC;
using DevExpress.Data.Summary;
using System.Data.SqlTypes;
//...
public class MyFilterController : ViewController<ListView> {
    private static readonly DateTime minDate;
    private static readonly DateTime maxDate;
    static MyFilterController() {
        minDate = (DateTime)SqlDateTime.MinValue;
        maxDate = (DateTime)SqlDateTime.MaxValue;
    }
    private Boolean CanFilter(string propertyName, string filterText) {
        IMemberInfo memberInfo = View.ObjectTypeInfo.FindMember(propertyName);
        if (SummaryItemTypeHelper.IsDateTime(memberInfo.MemberType)) {
            DateTime? convertedFilter = null;
            try {
                convertedFilter = Convert.ChangeType(filterText, typeof(DateTime)) as DateTime?;
            }
            catch {
                return false;
            }
            if (convertedFilter.HasValue) {
                if ((convertedFilter.Value < minDate) || (convertedFilter.Value > maxDate)) {
                    return false;
                }
            }
        }
        return true;
    }
    private ICollection<string> GetProcessedRequiredProperties(ICollection<string> searchProperties, 
string filterText) {
        List<string> result = new List<string>();
        foreach (string propertyName in searchProperties) {
           if (CanFilter(propertyName, filterText)) {
               result.Add(propertyName);
            }
        }
        return result;
    }
    private void FilterController_CustomGetFullTextSearchProperties(object sender, 
CustomGetFullTextSearchPropertiesEventArgs e) {
        string filterText = ((FilterController)sender).FullTextFilterAction.Value as string;
        if (!string.IsNullOrEmpty(filterText)) {
            ICollection<string> searchProperties = 
GetProcessedRequiredProperties(((FilterController)sender).GetFullTextSearchProperties(), filterText);
            e.Properties.AddRange(searchProperties);
            e.Handled = true;
        }
    }
    protected override void OnActivated() {
        base.OnActivated();
        FilterController filterController = Frame.GetController<FilterController>();
        if (filterController != null) {
            filterController.CustomGetFullTextSearchProperties += 
FilterController_CustomGetFullTextSearchProperties;
        }
    }
    protected override void OnDeactivated() {
        FilterController filterController = Frame.GetController<FilterController>();
        if (filterController != null) {
            filterController.CustomGetFullTextSearchProperties -= 
FilterController_CustomGetFullTextSearchProperties;
        }
        base.OnDeactivated();
    }
}
```
***
