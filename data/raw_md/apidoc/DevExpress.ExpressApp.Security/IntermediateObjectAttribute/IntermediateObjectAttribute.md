---
uid: DevExpress.ExpressApp.Security.IntermediateObjectAttribute
name: IntermediateObjectAttribute
type: Class
summary: Applies to classes. Marks the class as an intermediate in the [many-to-many relationship](xref:112654#technique-2-with-an-intermediate-object) declared with @DevExpress.Xpo.ManyToManyAliasAttribute.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class)]
    public class IntermediateObjectAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Security.IntermediateObjectAttribute._members
  altText: IntermediateObjectAttribute Members
---
The following example demonstrates how to apply this attribute:

# [C#](#tab/tabid-csharp)

```csharp{31}
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Xpo;
using System.Collections.Generic;
using System.ComponentModel;
// ...
[DefaultClassOptions]
public class Contact : XPObject {
    // ...
    [Browsable(false)]
    [Association("Contact-ContactTasks"), Aggregated]
    public XPCollection<ContactTask> ContactTasks { 
        get { return GetCollection<ContactTask>(nameof(ContactTasks)); } }
    [ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Task))]
    public IList<Task> TaskCollection {
        get { return GetList<Task>(nameof(TaskCollection)); }
    }
}
[DefaultClassOptions]
public class Task : XPObject {
    // ...
    [Browsable(false)]
    [Association("Task-ContactTasks"), Aggregated]
    public XPCollection<ContactTask> ContactTasks { 
        get { return GetCollection<ContactTask>(nameof(ContactTasks)); } }
    [ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Contact))]
    public IList<Contact> ContactCollection {
        get { return GetList<Contact>(nameof(ContactCollection)); }
    }
}
[IntermediateObject(nameof(Contact), nameof(Task))]
public class ContactTask : XPObject {
    public ContactTask(Session session) : base(session) { }
    Contact fContact;
    [Association("Contact-ContactTasks")]
    public Contact Contact {
        get { return fContact; }
        set { SetPropertyValue<Contact>(nameof(Contact), ref fContact, value); }
    }
    Task fTask;
    [Association("Task-ContactTasks")]
    public Task Task {
        get { return fTask; }
        set { SetPropertyValue<Task>(nameof(Task), ref fTask, value); }
    }
}
```
***