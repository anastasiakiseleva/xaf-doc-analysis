```csharp{<:0:>}
using DevExpress.Data.Filtering;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace YourSolutionName.Module.BusinessObjects;

[DefaultClassOptions]
public class MyPersistentClass : BaseObject {
    public virtual string Name { get; set; }
    public virtual bool IsNew { get; set; }
    public virtual ApplicationUser CreatedBy { get; set; }
    public virtual ApplicationUser LastModifiedBy { get; set; }
    ApplicationUser GetCurrentUser() {
        return ObjectSpace.FindObject<ApplicationUser>(CriteriaOperator.Parse("ID=CurrentUserId()"));
    }
    public override void OnCreated() {
        CreatedBy = GetCurrentUser();
        IsNew = true;
    }
    public override void OnLoaded() {
        IsNew = false;
    }
    public override void OnSaving() {
        if(ObjectSpace != null) {
            LastModifiedBy = GetCurrentUser();
        }
        IsNew = false;
    }
}

```