---
uid: "112797"
seealso: []
title: 'Upcasting (Combine Data from Base and Derived Classes)'
---
# Upcasting (Combine Data from Base and Derived Classes)

This topic demonstrates how to use [Upcasting](xref:2650) in XAF. This functionality is useful when you need to combine base and derived classes in a single query.

We suggest that you implement the following business model for this example:

![UpCasing1](~/images/upcasing1115575.png)

1. Expand the _MySolution.Module_ project and right-click the _Business Objects_ folder. Choose **Add | Class…**. Specify _UpcastingDataModel.cs_ as the new class name and click **Add**. Replace the auto-generated code with the following class declaration:

   # [EF Core](#tab/tabid-efcore)

   ```csharp
   using System;
   using DevExpress.Persistent.Base;
   using DevExpress.Persistent.BaseImpl.EF;
   using System.Collections.ObjectModel;

   namespace MySolution.Module.BusinessObjects {
      [DefaultClassOptions]
      [System.ComponentModel.DefaultProperty(nameof(Title))]
      public class Department : BaseObject {
         public virtual string Title { get; set; }
         public virtual string Office { get; set; }
         public virtual ICollection<EmployeeBase> Employees { get; set; } = new ObservableCollection<EmployeeBase>();
      }

      public abstract class EmployeeBase : BaseObject {
         public virtual string Name { get; set; }
         public virtual string Email { get; set; }
         public virtual Department Department { get; set; }
      }

      [DefaultClassOptions]
      public class LocalEmployee : EmployeeBase {
         public virtual string InsurancePolicyNumber { get; set; }
      }

      [DefaultClassOptions]
      public class ForeignEmployee : EmployeeBase {
         public virtual DateTime VisaExpirationDate {  get; set; }
      }
   }
   ```

   # [XPO](#tab/tabid-xpo)

   ```csharp
   using DevExpress.Persistent.Base;
   using DevExpress.Persistent.BaseImpl;
   using DevExpress.Xpo;

   namespace MySolution.Module.BusinessObjects;

   [DefaultClassOptions]
   [System.ComponentModel.DefaultProperty(nameof(Title))]
   public class Department : BaseObject {
      private string title;
      private string office;
      public Department(Session session) : base(session) { }
      public string Title {
         get { return title; }
         set {
               SetPropertyValue(nameof(Title), ref title, value);
         }
      }
      public string Office {
         get { return office; }
         set {
               SetPropertyValue(nameof(Office), ref office, value);
         }
      }
      [Association("Department-Employees")]
      public XPCollection<EmployeeBase> Employees {
         get { return GetCollection<EmployeeBase>(nameof(Employees)); }
      }
   }

   public class EmployeeBase : BaseObject {
      public EmployeeBase(Session session) : base(session) { }
      private string name;
      private string email;
      public string Name {
         get { return name; }
         set {
               SetPropertyValue(nameof(Name), ref name, value);
         }
      }
      public string Email {
         get { return email; }
         set {
               SetPropertyValue(nameof(Email), ref email, value);
         }
      }
      private Department department;
      [Association("Department-Employees")]
      public Department Department {
         get { return department; }
         set {
               SetPropertyValue(nameof(Department), ref department, value);
         }
      }
   }

   [DefaultClassOptions]
   public class LocalEmployee : EmployeeBase {
      public LocalEmployee(Session session) : base(session) { }
      private string insurancePolicyNumber;
      public string InsurancePolicyNumber {
         get { return insurancePolicyNumber; }
         set {
               SetPropertyValue(nameof(InsurancePolicyNumber), ref insurancePolicyNumber, value);
         }
      }
   }

   [DefaultClassOptions]
   public class ForeignEmployee : EmployeeBase {
      public ForeignEmployee(Session session) : base(session) { }
      private DateTime visaExpirationDate;
      public DateTime VisaExpirationDate {
         get { return visaExpirationDate; }
         set {
               SetPropertyValue(nameof(VisaExpirationDate), ref visaExpirationDate, value);
         }
      }
   }
   ```
   ***

   > [!TIP]
   > The `Department`, `LocalEmployee` and `ForeignEmployee` classes use the `DefaultClassOptions` attribute. For more information about this attribute, refer to the [Data Annotations in Data Model](xref:112701) topic.

2. If your application uses Entity Framework Core, register the following classes in the DbContext:

   **File:** _MySolution.Module\BusinessObjects\MySolutionDbContext_

   ```csharp
   using MySolution.Module.BusinessObjects;

   namespace  MySolution.Module.BusinessObjects {
      public class MySolutionEFCoreDbContext : DbContext {
         //...
         public DbSet<Department> Departments { get; set; }
         public DbSet<ForeignEmployee> ForeignEmployees { get; set; }
         public DbSet<LocalEmployee> LocalEmployees { get; set; }
      }
   }
   ```


3. Run the application and invoke the `Department` Detail View:

   ![|XAF ASP.NET Core Blazor - Detail View Before Configuration, DevExpress](~/images/upcasting3115577.png)

   The nested **Employees** List View only displays the `EmployeeBase` class's properties by default. Upcasting allows you to also display the `Employee` class descendant-specific properties.

4. To add required columns, invoke the [Model Editor](xref:112582). Navigate to the **Views | MySolution.Module.BusinessObjects | EmployeeBase | Department_Employees_ListView | Columns** node. Use the context menu to add two child nodes and assign the following values to the `PropertyName` properties of these nodes:

   * \<LocalEmployee>InsurancePolicyNumber 
   * \<ForeignEmployee>VisaExpirationDate

   XAF recognizes these values and displays the `LocalEmployee.InsurancePolicyNumber` and `ForeignEmployee.VisaExpirationDate` properties for the objects retrieved from the database to populate the `Department.Employees` collection.

5. Run the application and invoke the `Department` Detail View. XAF now displays the properties of the `EmployeeBase` class and its descendants.

   ![|XAF ASP.NET Core Blazor - Detail View After Configuration, DevExpress](~/images/upcasting2115576.png)
