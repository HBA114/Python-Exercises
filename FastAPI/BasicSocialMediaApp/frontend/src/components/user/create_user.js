import React, { useEffect, useState } from "react";
import data from "../../myData.json"

const defaultImageSrc = "/img/person-icon.png"
const userRequestAddress = data["user"]

const initialUserData = {
    userId: 0,
    userEmail: '',
    userPassword: '',
    imageStr: '',
    imageSrc: defaultImageSrc,
    imageFile: null
}

export default function CreateUser() {
    const [values, setValues] = useState(initialUserData)

    useEffect(() => {
    }, [])

    const getBase64 = (file, cb) => {
        let reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function () {
            cb(reader.result)
        };
        reader.onerror = function (error) {
            console.log('Error: ', error);
        };
    }

    const handleInputChange = e => {
        const { name, value } = e.target

        setValues({
            ...values,
            [name]: value
        })
    }

    const showPreview = e => {
        if (e.target.files && e.target.files[0] && e.target.files[0].size < 409600) {
            let imageFile = e.target.files[0]

            const reader = new FileReader()

            reader.onload = x => {
                setValues({
                    ...values,
                    imageFile,
                    imageSrc: x.target.result
                })
                console.log(imageFile.size / 1024 + " kb"); //!!
            }

            reader.readAsDataURL(imageFile)
            getBase64(imageFile, (result) => {
                setValues({
                    ...values,
                    imageStr: result
                })
                console.log(result)
            })
        }
        else {
            console.log("please select a image that less than 400 kb.")
            setValues({
                ...values,
                imageFile: null,
                imageSrc: defaultImageSrc,
                imageStr: ''
            })
        }
    }

    const sendData = async () => {
        await fetch(
            userRequestAddress,
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email: values.userEmail,
                    photo_base64: values.imageStr,
                    password: values.userPassword
                })
            }
        )
    }

    const submitForm = e => {
        e.preventDefault()
        sendData()
    }

    return (
        <div>
            <form autoComplete="off" noValidate className="text-center" onSubmit={submitForm}>
                <div className="card">
                    <div className="text-center">
                        <img height='200px' src={values.imageStr === '' ? values.imageSrc : values.imageStr} alt="deneme"
                            className="card-image-top rounded-circle" />
                    </div>
                    <div className="card-body">
                        <div className="form-group">
                            <input type="file" accept="image/*" className="form-control-file"
                                onChange={showPreview} id="image-uploader" />
                        </div>
                        <div className="form-group">
                            <input className="form-control" placeholder="Email Address" name="userEmail"
                                value={values.userEmail} onChange={handleInputChange} />
                        </div>
                        <div className="form-group">
                            <input className="form-control" placeholder="Password" name="userPassword"
                                value={values.userPassword} onChange={handleInputChange} />
                        </div>
                        <div className="form-group text-center">
                            <button type="submit" className="btn btn-light">Submit</button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    )
}