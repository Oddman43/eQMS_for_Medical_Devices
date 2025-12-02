# SOP-001 Document Control Procedure

## 1\. Purpose

The purpose of this procedure is to define the controls needed to approve, review, update, and manage the lifecycle of documents within the Quality Management System (QMS). This ensures compliance with ISO 13485:2016 (Sec 4.2.4), MDR (EU) 2017/745, IVDR (EU) 2017/746, and 21 CFR Part 820.40. This procedure also addresses requirements for electronic records and signatures per 21 CFR Part 11.

## 2\. Scope

This procedure applies to all internal and external documents required by the QMS and Regulatory Authorities.

- In Scope: Quality Manual, SOPs, Work Instructions, Forms (templates), Policies, Technical Documentation specifications.

- Out of Scope: Specific Records (filled forms) are controlled under the *Control of Records Procedure*, although this system manages their storage.

## 3\. Definitions

- Controlled Document: A document that dictates a process or specification (e.g., SOP, Policy). Changes require approval.

- Record: Evidence of results achieved or activities performed (e.g., a signed Audit Report). Records are immutable.

- Effective Date: The date on which the document becomes official and must be followed. This allows a training window between Approval and Effectiveness.

- Audit Trail: A secure, computer-generated, time-stamped electronic record that allows reconstruction of the course of events relating to the creation, modification, or deletion of an electronic record.

- Master Document List: The Master Document List (MDL) is an automatically generated list produced by the eQMS. It reflects the latest status, version, and metadata of all controlled documents. No manual editing of the MDL is allowed.

## 4\. Roles and Responsibilities

### 4\.1 Document Control Officer (DCO) / Quality Assurance (QA)

- Administer the electronic QMS (eQMS).

- Assign Document Numbers.

- Maintain the Master Document List (MDL).

### 4\.2 Document Owner / Author

- Draft and revise documents.

- Ensure technical accuracy.

- Determine the training requirements for the document.

### 4\.3 Approvers

- Review documents for adequacy and compliance.

- Provide electronic approval/signature.

## 5\. Document Lifecycle Definitions

The QMS utilizes a lifecycle approach to document management. The Electronic QMS (eQMS) automatically assigns and controls the following statuses:

| Status                 | Definition                                                                                                                            | Access Rights                                       |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **DRAFT**              | Document is being created or revised. Content is not final.                                                                           | **Edit:** Owner. **Read:** Owner, Approvers         |
| **IN REVIEW**          | Document is locked for editing and is undergoing technical and quality review.                                                        | **Edit:** None (Comments only). **Read:** Reviewers |
| **APPROVED - PENDING** | Document is signed and approved but strictly waiting for the Effective Date or completion of training. Not valid for operational use. | **Edit:** None. **Read:** Training Mgr, QA          |
| **RELEASED**           | The official, effective version of the document to be used for QMS activities.                                                        | **Edit:** None. **Read:** All Employees             |
| **SUPERSEDED**         | A previous version of a document that has been replaced by a newer released version. Retained for historical traceability.            | **Edit:** None. **Read:** QA/Admin only             |
| **OBSOLETE**           | The document has been withdrawn from use entirely and is no longer applicable to the QMS.                                             | **Edit:** None. **Read:** QA/Admin only             |

## 6\. Procedure

### 6\.1 Document Creation and Identification

1. All documents must be drafted using the approved Standard Template.

2. The eQMS (Python System) shall automatically assign a unique identifier following the format: `TYPE-XXX` (e.g., `SOP-001`).

3. Draft Status: Documents in the drafting phase are watermarked as "DRAFT" and are not valid for use.

### 6\.2 Review and Approval

1. Documents must be reviewed for adequacy prior to issue.

2. Approver Matrix:

    - SOPs/Policies: Require Author + Department Manager + Quality Manager.

    - Work Instructions: Require Author + Area Supervisor + Quality Assurance.

3. Electronic Signature (21 CFR Part 11 Compliance):

    - The system must enforce re-entry of password/credentials to execute approval.

    - The signature block must visibly display:

        - Printed Name of the signer.

        - Date and Time (timestamp).

        - Meaning of signature (e.g., "I approve this document").

### 6\.3 Training and Effective Date

1. Upon Approval, the document status changes to "APPROVED - PENDING TRAINING".

2. The system calculates the Effective Date.

    - Standard: Approval Date + 14 days (to allow for training).

    - Urgent: Can be immediate if justification is provided and training is verified.

3. Notifications are sent to affected users.

### 6\.4 Document Release and Distribution

1. On the Effective Date, the system automatically:

    - Moves the document status to "RELEASED / CURRENT".

    - Moves the previous version to "SUPERSEDED".

    - Updates the Master Document List (MDL).

2. Access Control: Only "RELEASED" documents are visible to general users (Read-Only). "OBSOLETE" documents are visible only to QA/Admin with a visible "OBSOLETE" watermark.

### 6\.5 Change Control (Version Control)

1. Changes require a formal Change Request (CR) in the system.

2. The Author must describe:

    - Reason for change.

    - Description of change.

    - Impact assessment (Regulatory, Risk, Validation).

3. Revision History: The system must append a row to the revision history table of the document automatically.

4. Major changes (affecting form, fit, function, or safety) increment the integer (Rev 1.0 → Rev 2.0). Minor corrections increment the decimal (Rev 1.0 → Rev 1.1) only if defined in the policy.

### 6\.6 Control of External Documents

1. External Standards (ISO, MDR, CFR) are logged in the External Document List.

2. QA reviews these annually to ensure the latest version is applicable.

### 6\.7 Document Retention and Archiving

1. Obsolescence: If a document is no longer required (e.g. process discontinued), the Document Owner must initiate a Change Request to change the status from "RELEASED" directly to "OBSOLETE".

2. Obsolete and Superseded documents are retained electronically for at least the lifetime of the medical device plus two (2) years, or as required by local regulations, whichever is longer.

3. The system must ensure backups prevent data loss.

4. Deletion of records is strictly prohibited unless authorized by Top Management and technically executed in a way that preserves the Audit Trail of the deletion.

## 7\. Electronic System Requirements (Technical Specs for QA)

To ensure compliance with 21 CFR Part 11, the Python/SQL system includes:

- Audit Trails: Any creation, modification, or deletion of a document triggers an immutable SQL log entry (Who, What, When, Why, Old Value, New Value).

- Security: User sessions time out after inactivity. Passwords must be strong and rotated.

- Data Integrity: SQL transactions ensure data is not corrupted during status changes.\`
