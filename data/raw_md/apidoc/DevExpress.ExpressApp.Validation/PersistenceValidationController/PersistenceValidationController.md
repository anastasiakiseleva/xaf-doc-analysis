---
uid: DevExpress.ExpressApp.Validation.PersistenceValidationController
name: PersistenceValidationController
type: Class
summary: Validates persistent objects when they are saved or deleted in the UI.
syntax:
  content: 'public class PersistenceValidationController : ViewController'
seealso:
- linkId: DevExpress.ExpressApp.Validation.PersistenceValidationController._members
  altText: PersistenceValidationController Members
- linkId: "113684"
- linkId: "113251"
---
This [Controller](xref:112621) is activated in root [Detail Views and List Views](xref:112611). 
To provide validation in the particular Context, the Controller subscribes to the [IObjectSpace.Committing](xref:DevExpress.ExpressApp.IObjectSpace.Committing) and [IObjectSpace.CustomDeleteObjects](xref:DevExpress.ExpressApp.IObjectSpace.CustomDeleteObjects) event of the current View's [Object Space](xref:113707). The table below contains peculiarities of this process in the **Save** and **Delete** [contexts](xref:DevExpress.Persistent.Validation.DefaultContexts) .


|                   |  Save Context    | Delete Context  |
|-------------------|------------------|-----------------|
| **Handled event**             | [IObjectSpace.Committing](xref:DevExpress.ExpressApp.IObjectSpace.Committing) | [IObjectSpace.CustomDeleteObjects](xref:DevExpress.ExpressApp.IObjectSpace.CustomDeleteObjects) |
| **Validated objects** | The [View.CurrentObject](xref:DevExpress.ExpressApp.View.CurrentObject), its aggregated objects and other modified objects. | The objects marked for deletion and their aggregated objects.|
| **Event handler behavior**          | The Controller checks all validation rules from the [RuleSet.RegisterRules](xref:DevExpress.Persistent.Validation.RuleSet.RegisterRules(DevExpress.ExpressApp.DC.ITypeInfo)) collection associated with the **Save** validation context. If at least one rule is broken, the Controller cancels the Save [Action](xref:112622) execution and raises a validation exception. | The Controller checks all validation rules associated with the **Delete** validation context. If at least one rule is broken, the Controller cancels the Delete [Action](xref:112622) execution and raises a validation exception. |
| **Failed validation result** | New and modified objects are not saved to the database. The current Object Space and all editors have the same state as before committing. | No objects are deleted from the database. The current View and Object Space stay unchanged. |
| **Passed validation result** | All new and modified objects are saved to the database. | All objects that are marked for deletion are deleted in the current Object Space, and will be deleted from the database after the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method execution. This method is executed immediately if the [DeleteObjectsViewController.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.AutoCommit) property is **true**. Otherwise, the **CommitChanges** method is executed when you save changes. |

![Validation_Save_Win](~/images/validation_save_win116605.png)

![Validation_Save_Web](~/images/validation_save_web116607.png)

The **PersistenceValidationController** exposes several events that allow you to customize the default validation process.

| Event | Description |
|---|---|
| [PersistenceValidationController.ContextValidating](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController.ContextValidating) | Handle this event to modify the collection of objects which will be validated in the current context. |
| [PersistenceValidationController.CustomGetAggregatedObjectsToValidate](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController.CustomGetAggregatedObjectsToValidate) | Handle this event to manually specify aggregated objects to be validated. |
| [PersistenceValidationController.NeedToValidateObject](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController.NeedToValidateObject) | Handle this event to exclude particular objects from validation. |

The example below demonstrates how you can use the [](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController) class and the events described in the table above.

For example, adjust the rules for the **Person** class, which has an aggregated collection of **Address** objects and a non-aggregated collection of the **Story** objects. The code snippet below demonstrates these classes decorated with the [](xref:DevExpress.Persistent.Validation.RuleCriteriaAttribute).

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Validation;
using System.Collections.ObjectModel;
using System.COmponentModel.DataAnnotations;
//...
[DefaultClassOptions]
[RuleCriteria("AssressRule", DefaultContexts.Save, "City == 'Tokyo' or Owner.Name != 'Sam'", 
"Address message", SkipNullOrEmptyValues = false)]
public class Address : BaseObject {
    public virtual string City { get; set; }
    public virtual Person Owner { get; set; }
}

[DefaultClassOptions]
[RuleCriteria("PersonRule", DefaultContexts.Save, "Name != 'John'", 
"Person message", SkipNullOrEmptyValues = false)]
public class Person : BaseObject {
    public virtual string Name { get; set; }
    public virtual IList<Address> Addresses { get; set; } = new ObservableCollection<Address>();
    public virtual IList<Story> Stories { get; set; } = new ObservableCollection<Story>();
}

[DefaultClassOptions]
[RuleCriteria("HistoryRule", DefaultContexts.Save, "Owner == null or Owner.Name != 'Bob'", 
"History message", SkipNullOrEmptyValues = false)]
public class Story : BaseObject {
    public virtual string StoryText { get; set; }
    public virtual Person Owner { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Validation;
using DevExpress.Xpo;
//...
[DefaultClassOptions]
[RuleCriteria("AssressRule", DefaultContexts.Save, "City == 'Tokyo' or Owner.Name != 'Sam'", 
"Address message", SkipNullOrEmptyValues = false)]
public class Address : XPObject {
    private string city;
    public string City {
        get { return city; }
        set { SetPropertyValue(nameof(City), ref city, value); }
    }
    public Address(Session session)
        : base(session) {
    }
    private Person owner;
    [Association("PersonAddresses")]
    public Person Owner {
        get { return owner; }
        set { SetPropertyValue(nameof(Owner), ref owner, value); }
    }
}
[DefaultClassOptions]
[RuleCriteria("PersonRule", DefaultContexts.Save, "Name != 'John'", 
"Person message", SkipNullOrEmptyValues = false)]
public class Person : XPObject {
    public Person(Session session)
        : base(session) {
    }
    private string name;
    public string Name {
        get { return name; }
        set { SetPropertyValue(nameof(Name), ref name, value); }
    }
    [DevExpress.Xpo.Aggregated, Association("PersonAddresses")]
    public XPCollection<Address> Addresses {
        get { return GetCollection<Address>(nameof(Addresses)); }
    }
    [Association("PersonStory")]
    public XPCollection<Story> Stories {
        get { return GetCollection<Story>(nameof(Stories)); }
    }
}
[DefaultClassOptions]
[RuleCriteria("HistoryRule", DefaultContexts.Save, "Owner == null or Owner.Name != 'Bob'", 
"History message", SkipNullOrEmptyValues = false)]
public class Story : XPObject {
    private string story;
    public string StoryText {
        get { return story; }
        set { SetPropertyValue(nameof(StoryText), ref story, value); }
    }
    public Story(Session session)
        : base(session) {
    }
    private Person owner;
    [Association("PersonStory")]
    public Person Owner {
        get { return owner; }
        set { SetPropertyValue(nameof(Owner), ref owner, value); }
    }
}
```
***

The following rules are formed for validating the objects above.

* The **Address** objects do not need to be validated if their **City** property is set to **Tokyo**.
* Aggregated objects need to be validated if the root object is modified.
* When the current object is **Person**, it is validated only if this object was modified. Aggregated objects modifications are ignored.
* If the **Person** object is modified, all objects from its **Stories** collection are checked.

Create a new controller which uses the [](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController) controller to validate objects depending on the rules above. The **NeedToValidateObject** event is handled here to specify whether the objects with a particular property value need to be validated or not. The **CustomGetAggregatedObjectsToValidate** event is used to modify a collection of aggregated objects to validate. The **ContextValidating** event allows organizing a collection of all objects to be validated in the particular context.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Validation;
//...
public class CustomValidationController : ViewController {
    PersistenceValidationController pController;
    protected override void OnActivated() {
        base.OnActivated();
        pController = Frame.GetController<PersistenceValidationController>();
        if(pController != null) {
            pController.ContextValidating += PController_ContextValidating;
            pController.NeedToValidateObject += PController_NeedToValidateObject;
            pController.CustomGetAggregatedObjectsToValidate += 
PController_CustomGetAggregatedObjectsToValidate;
        }
    }
    private void PController_CustomGetAggregatedObjectsToValidate(object sender, 
CustomGetAggregatedObjectsToValidateEventArgs e) {
        if(!ObjectSpace.IsObjectToSave(e.OwnerObject)) {
            e.Handled = true;
        }
    }
    private void PController_NeedToValidateObject(object sender, NeedToValidateObjectEventArgs e) {
        if(e.CurrentObject is Address && ((Address)e.CurrentObject).City == "Tokyo") {
            e.NeedToValidate = false;
        }
    }
    private void PController_ContextValidating(object sender, ContextValidatingEventArgs e) {
        Person person = View.CurrentObject as Person;
        if (e.Context.Id == "Save" && person != null) {
            if (ObjectSpace.IsObjectToSave(person)) {
                foreach (object obj in person.Stories) {
                    e.TargetObjects.Add(obj);
                }
            }
            else {
                e.TargetObjects.Remove(person);
            }
        }
    }
}
```
***