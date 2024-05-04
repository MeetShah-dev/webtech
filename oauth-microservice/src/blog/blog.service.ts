import { HttpService } from '@nestjs/axios';
import { Injectable } from '@nestjs/common';
import { firstValueFrom } from 'rxjs';
import axios from "axios"
import FormData from 'form-data';

const BLOGGING_API = process.env.BLOGGING_API
const NOTIFICATION_API = process.env.NOTIFICATION_API
@Injectable()
export class BlogService {
    constructor(
        private httpService: HttpService
    ) { }
    async createBlog(req, res, files) {
        const formData = new FormData();

        // Append file data if files exist
        files.forEach((file, index) => {
            const fieldName = `file${index + 1}`;
            formData.append(file.fieldname = fieldName, file.buffer, file.originalname);
        });
        console.log("filess---", req)
        // Append other payload data
        let payload = { ...req.body, "user": req.user.id.toString() };
        Object.keys(payload).forEach(key => {
            formData.append(key, payload[key]);
        });

        console.log("FORM DATA--", formData)
        try {
            const response = await this.httpService.post(`${process.env.BLOGGING_API}create-blog/`, formData, {
                headers: {
                    ...formData.getHeaders(),
                },
            }).toPromise();

            return res.json(response.data);
        } catch (e) {
            console.log("error", JSON.stringify(e));
            res.status(500).send('Failed to create blog');
        }

    }

    async getLatestMagazine(req, res) {
        const response = await firstValueFrom(this.httpService.get(BLOGGING_API + 'magazine-feed/'));
        return res.json(response.data);
    }
    async getArchiveMagazine(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'archived-magazine/', {
                params: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getUserReadBlog(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-user-blogs/', {
                params: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getUserDrafts(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-drafts/', {
                params: {
                    user: req.user.id.toString()
                }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getReadBlog(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-blog/', {

                params: {
                    ...req.body,
                    user: req.user.id.toString()
                },
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async updateBlog(req, res, files) {
        const formData = new FormData();
        files.forEach((file, index) => {
            const fieldName = `file${index + 1}`;
            formData.append(file.fieldname = fieldName, file.buffer, file.originalname);
        });
        let payload = { ...req.body, "user": req.user.id.toString() };
        Object.keys(payload).forEach(key => {
            formData.append(key, payload[key]);
        });
        try {
            const response = await this.httpService.put(`${process.env.BLOGGING_API}update-blog/`, formData, {
                headers: {
                    ...formData.getHeaders(),
                },
            }).toPromise();

            return res.json(response.data);
        } catch (e) {
            console.log("error", JSON.stringify(e));
            res.status(500).send('Failed to create blog');
        }
    }
    async deleteBlog(req, res) {
        try {
            const response: any = await axios.delete(BLOGGING_API + 'delete-blog/', {
                data: { ...req.body, "user": req.user.id.toString() }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async deleteFile(req, res) {
        try {
            const response: any = await axios.delete(BLOGGING_API + 'delete-file/', {
                data: { ...req.body, "user": req.user.toString() }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getReadUserRejectedBlogs(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-user-rejected-blogs/', {
                params: { "user": req.user.id.toString() }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async addReader(req, res) {
        let payload = req.body;
        payload = { ...payload, "user": req.user.id.toString() }
        try {
            const response = await firstValueFrom(this.httpService.post(BLOGGING_API + 'add-reader/', payload, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async getUserNotifications(req, res) {
        try {
            const response: any = await axios.get(NOTIFICATION_API + 'user-notifications/', {
                params: { "user": req.user.id.toString() }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async readBlogModeration(req, res) {
        try {
            const response: any = await axios.get(`${process.env.BLOGGING_API}read-blog-moderation/`, {
                params: { ...req.body }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
}
