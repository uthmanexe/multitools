
import qrcode
import subprocess
import pathlib as path


def qrcodify():
    # FIX: All lines are now properly indented inside the function body
    print("\n")
    print("=====================================")
    print("          QR Code Generator          ")
    print("=====================================")
    text = input("Enter text to qrcodify: ").strip()

    if not text:
        print("No text provided. Cancelling.")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=7,
        border=1,
    )
    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")

    # Current directory for the image and temporary save to view:
    tmpfile = path.Path("qr.png")
    image.save(tmpfile)
    subprocess.run(["viu", "-w", "45", str(tmpfile)])

    # Do I want to save the file?:
    save = input("\nSave QR Code? (y/n): ").strip().lower()
    if save == "y":
        name = input("File name: ").strip()
        # if no name: give a default name
        if not name:
            name = "qr"

        # Do I want to save it in a different directory?:
        redirect = input("Save in current directory? (y/n): ").strip().lower()
        if redirect == "y":
            target_dir = path.Path.cwd()
        else:
            new_path = input("Enter target directory path: ").strip()
            target_dir = path.Path(new_path)
            
            # Just in case the directory doesn't exist yet:
            target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / f"{name}.png"

        # But if it does: 
        while target_file.exists():
            print(f"File '{target_file.name}' already exists in that directory.")
            name = input("Enter a new file name: ").strip()
            if not name:
                name = "qr_copy"
            target_file = target_dir / f"{name}.png"

        tmpfile.rename(target_file)
        print(f"File has been successfully saved to: {target_file}")

    else:
        if tmpfile.exists():
            tmpfile.unlink()
        print("QR Code has been deleted.")
